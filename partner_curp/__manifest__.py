# -*- coding: utf-8 -*-
{
    'name': "partner_curp/odoo17",
    'summary': "modulo para poder asignar las curps en odoo17",
    'description': """
modulo para poder asignar las curps en odoo17
    """,
    'author': "dania",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'mail'],
    'data': [
       'views/partner_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_tests': [
            'contacts/static/tests/tours/**/*',
        ],
    }
}

