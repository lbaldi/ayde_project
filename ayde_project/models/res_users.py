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


class ResUsers(models.Model):

    _inherit = 'res.users'

    salary = fields.Float(
        string="Salario",
        required=True,
    )

    @api.one
    @api.constrains('salary')
    def _check_salary(self):
        if self.salary <= 0.0:
            raise Warning("El valor debe ser mayor igual a 0.")

    def get_cost(self):
        cost = 0
        cost += self.company_id.get_it_expense_by_user()
        cost += self.salary / 12
        cost += self.salary * self.company_id.it_expense
        return cost

ResUsers()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
