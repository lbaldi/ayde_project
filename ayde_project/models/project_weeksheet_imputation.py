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


class ProjecWeeksheetImputation(models.Model):

    _name = 'project.weeksheet.imputation'

    _description = 'Imputacion'

    project_weeksheet_id = fields.Many2one(
        comodel_name='project.weeksheet',
        string="Dedicacion Semanal",
        required=True,
    )

    project_id = fields.Many2one(
        comodel_name='project.project',
        string="Proyecto",
        required=True,
    )

    percentage = fields.Float(
        string="Porcentaje",
        required=True,
    )

    @api.one
    @api.constrains('percentage')
    def _check_percentage(self):
        if self.percentage <= 0.0 or self.percentage > 100.0:
            raise Warning("El porcentaje establecido debe ser mayor a 0 y menor igual que 100!")


    _sql_constraints = [
        ('unique_week_project',
         'unique(project_id,project_weeksheet_id)',
         "Ya existe una imputacion para este proyecto en esta ficha de dedicacion semanal!"
        )
    ]

ProjecWeeksheetImputation()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
