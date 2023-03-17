# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'shield_senegal',
    'version': '15.0.0.0',
    'category': "Project",
    'license': 'OPL-1',
    'summary': 'This apps helps to make project as template and make new project from the Template',
    'description': """Project Template , Make project as template and make new project from the Template, """,
    'author': 'Abdou NDAO',
    'website': 'https://www.shieldsenegal.sn',
    'depends': ['base', 'project', 'sale', 'purchase', 'account', 'code_backend_theme'],
    'data': [
        'views/meca_services_form.xml',
        'views/meca_services_tree_action.xml',
        'views/sequences.xml',
        'views/meca_menu.xml',
        'security/ir.model.access.csv',

    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    "images": ['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
