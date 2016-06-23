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


class ResCompany(models.Model):

    _inherit = 'res.company'

    tax_percentage = fields.Float(
        string="Porcentaje Cargas Sociales",
        required=True,
    )

    def get_tax_multiplier(self):
        return 1 + (self.tax_percentage / 100)

    @api.one
    @api.constrains('tax_percentage')
    def _check_tax_percentage(self):
        if self.tax_percentage <= 0.0 or self.tax_percentage > 100.0:
            raise Warning("El porcentaje establecido debe ser mayor a 0 y menor igual que 100!")

    it_expense = fields.Float(
        string="Gastos Fijos",
        required=True,
    )

    @api.one
    @api.constrains('it_expense')
    def _check_it_expense(self):
        if self.it_expense <= 0.0:
            raise Warning("El valor debe ser mayor igual a 0.")


    user_ids = fields.One2many(
        comodel_name='res.users',
        inverse_name="company_id",
        string = "Usuarios",
    )

    def get_it_expense_by_user(self):
        if self.user_ids:
            return self.it_expense / len(self.user_ids)
        else:
            return 0

ResCompany()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
