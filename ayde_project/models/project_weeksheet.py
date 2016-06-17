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

    name = fields.Char(
        string="Nombre",
        required=True,
    )

    period_id = fields.Many2one(
        commodelname='project.period',
        string="Periodo",
        required=True,
    )

    week = fields.Selection(
        [
            ('1', '1 - Primer Semana'),
            ('2', '2 - Segunda Semana'),
            ('3', '3 - Tercer Semana') ,
            ('4', '4 - Cuarta Semana')
        ],
        string="Semana",
        required=True,
    )

    user_id = fields.Many2one(
        commodelname='res.users',
        string="Usuario",
        required=True,
    )

    _sql_constraints = [
        ('unique_week_period',
         'unique(period_id,week,user_id)',
         "Ya existe una ficha de dedicacion semanal para este usuario, periodo y semana!"
        )
    ]

ProjecWeeksheet()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
