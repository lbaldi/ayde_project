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


class ProjectProject(models.Model):

    _name = 'project.project'

    _description = 'Proyecto'

    name = fields.Char(
        string="Nombre",
        required=True,
    )

    visible = fields.Boolean(
        string="Visible en reporte de costo?"
    )

    highlight = fields.Boolean(
        string="Resaltar en reporte de costo?",
        default=False,
    )

    active = fields.Boolean(
        string="Activo",
        default=True,
    )

ProjectProject()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
