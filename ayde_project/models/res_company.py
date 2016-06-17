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

    it_expense = fields.Float(
        string="Gastos Infraestructura",
        required=True,
    )

ResCompany()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
