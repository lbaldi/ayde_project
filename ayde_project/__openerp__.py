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
{

    'name': 'AYDE Project',

    'version': '1.0',

    'category': 'custom',

    'summary': 'AYDE Project Cost Module',

    'author': 'nibble',

    'website': 'https://github.com/lbaldi/ayde_project',

    'depends': [

        'base',

    ],

    'data': [

        'data/res_group.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/project_project.xml',
        'views/res_users.xml',
        'views/res_company.xml',
        'views/project_period.xml',
        'views/project_weeksheet.xml',
        'wizard/project_cost_report_wizard.xml',

    ],

    'installable': True,

    'auto_install': False,

    'application': True,

    'description': """
AYDE Project
======================================
* Project
* WeekSheet
* Imputations
* Project Cost Report
""",

}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
