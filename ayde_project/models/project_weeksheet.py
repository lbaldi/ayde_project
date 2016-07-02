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


class ProjecWeeksheet(models.Model):

    _name = 'project.weeksheet'

    _description = 'Dedicacion Semanal'

    period_id = fields.Many2one(
        comodel_name='project.period',
        string="Periodo",
        required=True,
    )

    week = fields.Selection(
        [
            ('1', '1 - Primer Semana  ( 01 a 07 )'),
            ('2', '2 - Segunda Semana ( 08 a 15 )'),
            ('3', '3 - Tercer Semana  ( 16 a 23 )'),
            ('4', '4 - Cuarta Semana  ( 24 a 30 )')
        ],
        string="Semana",
        required=True,
    )

    user_id = fields.Many2one(
        comodel_name='res.users',
        string="Usuario",
        required=True,
        default=lambda self: self.env.user,
    )

    imputation_ids = fields.One2many(
        comodel_name='project.weeksheet.imputation',
        inverse_name="project_weeksheet_id",
        string = "Imputaciones",
    )

    def get_cost(self):
        return self.user_id.get_cost() / 4

    @api.one
    @api.constrains('imputation_ids')
    def _check_percentage(self):
        total = 0
        for imputation in self.imputation_ids:
            total += imputation.percentage
        if total != 100:
            raise Warning("La sumatoria de todas las imputaciones debe ser igual a 100")

    @api.models
    def unlink(self):
        if self.period_id.unlink_date > fields.Datetime.now():
            raise Warning("No se puede eliminar esta ficha de dedicacion")

    _sql_constraints = [
        ('unique_week_period',
         'unique(period_id,week,user_id)',
         "Ya existe una ficha de dedicacion semanal para este usuario, periodo y semana!"
        )
    ]

ProjecWeeksheet()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
