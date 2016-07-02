# - coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
from openerp.exceptions import Warning

import locale
locale.setlocale(locale.LC_ALL, '')

import emailSender

import logging
_logger = logging.getLogger(__name__)


class ProjectCostReportWizard(models.TransientModel):

    _name = 'project.cost.report.wizard'

    _description = 'Reporte de costo de proyectos'

    @api.one
    def send_notification(self):

        if self.project_period_id:

            recipients = []

            for user in self.env.user.company_id.user_ids:

                weeksheets = self.project_period_id.weeksheet_ids.filtered(lambda  i: i.user_id == user)
                if len(weeksheets) < 4:
                    recipients.append(user.email_notification)

            body = 'Se solicita la carga de dedicacion pendiente del periodo {period}'.format(
                period=self.project_period_id.name,
            )

            if recipients:

                try:

                    emailSender.emailSender.send_email(
                        smtp=self.env.user.company_id.mail_smtp,
                        port=self.env.user.company_id.mail_port,
                        email=self.env.user.company_id.mail_mail,
                        password=self.env.user.company_id.mail_password,
                        recipient=recipients,
                        subject="Notificacion",
                        body=body,
                    )

                except:

                    raise Warning('Ha ocurrido un error al enviar el mensaje.')

        else:
            raise Warning("Debe seleccionar un periodo para ejecutar esta acccion.")

    @api.onchange('project_period_id')
    def onchange_project_period_id(self):

        # CALCULO % DE CARGA.
        max_weeksheet = 4 * len(self.env.user.company_id.user_ids)
        count_weeksheet = len(self.project_period_id.weeksheet_ids)
        percentage_weeksheet = int(float(count_weeksheet) / float(max_weeksheet) * 100)

        buffer_string = '<p>El porcentaje de carga es del {} %</p>'.format(percentage_weeksheet)

        buffer_string += \
            '<table border="1" style="width:100%">' \
                '<tbody>' \
                    '<tr>' \
                        '<td><span style="font-weight: bold;">Proyecto</span></td>' \
                        '<td><span style="font-weight: bold;">Costo</span></td>' \
                    '</tr>'

        buffer_string_ending = \
                '</tbody>' \
            '</table>' \
            '<p>* Los proyectos resaltados son proyectos internos.</p>'

        buffer_squeleton = \
            '<tr> \
                <td bgcolor="{color}">{name}</td> \
                <td style="text-align: right!important" bgcolor="#a1acfb">${cost}</td> \
            </tr>'

        if self.project_period_id:

            imputations = self.env['project.weeksheet.imputation']

            for weeksheet in self.project_period_id.weeksheet_ids:

                imputations = imputations | weeksheet.imputation_ids

            imputations = imputations.filtered("project_id.visible")

            projects = imputations.mapped('project_id')

            for project in projects:

                cost = 0
                color = '#FFFFFF'

                if project.highlight:
                    color = '#ce5656'

                project_imputations = imputations.filtered(lambda i: i.project_id == project)

                for project_imputation in project_imputations:

                    cost += project_imputation.get_cost()

                buffer_string += buffer_squeleton.format(
                    color=color,
                    name=project.name,
                    cost=locale.format('%.f', cost, True),
                )

            buffer_string += buffer_string_ending

        else:
            buffer_string = 'Debe elegir un periodo para visualizar el reporte.'

        self.text_report = buffer_string

    project_period_id = fields.Many2one(
        comodel_name="project.period",
        string="Periodo",
        required=True,
    )

    text_report = fields.Text(
        string="Reporte"
    )

ProjectCostReportWizard()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
