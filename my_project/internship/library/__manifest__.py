# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Booki',
    'version': '1.0',
    'category': 'Library',
    'sequence': 1,
    'summary': 'Managing Library',
    'description': """
        Add Book
    """,
    'website': 'https://www.quantum-space.co/',
    'depends': ['base',],
    'data': [
        #'security/hr_referral_security.xml',
        'security/ir.model.access.csv',

        'views/book_views.xml'

    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}
