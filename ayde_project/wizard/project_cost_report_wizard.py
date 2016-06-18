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

import logging
_logger = logging.getLogger(__name__)


class ProjectCostReportWizard(models.TransientModel):

    _name = 'project.cost.report.wizard'

    _description = 'Reporte de costo de proyectos'

    @api.onchange('project_period_id')
    def onchange_project_period_id(self):

        buffer_string = ''
        buffer_squeleton = '{name}: ${cost}\n'

        if self.project_period_id:

            imputations = self.env['project.weeksheet.imputation']

            for weeksheet in self.project_period_id.weeksheet_ids:

                imputations = imputations | weeksheet.imputation_ids

            imputations = imputations.filtered("project_id.visible")

            projects = imputations.mapped('project_id')

            for project in projects:

                cost = 0

                project_imputations = imputations.filtered(lambda i: i.project_id == project)

                for project_imputation in project_imputations:

                    cost += project_imputation.get_cost()

                buffer_string += buffer_squeleton.format(
                    name=project.name,
                    cost=round(cost,2),
                )

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
