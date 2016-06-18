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
        if self.project_period_id:
            buffer_string += 'Proyecto 1: $1324123.0\n'
            buffer_string += 'Proyecto 2: $23.0\n'
            buffer_string += 'Proyecto 3: $133.0\n'
            buffer_string += 'Proyecto 4: $1322344123.0\n'
            buffer_string += 'Proyecto 6: $234.0\n'
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

    @api.one
    def getReport(self):
        pass

ProjectCostReportWizard()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
