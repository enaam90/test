# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'schooli',
    'version': '1.0',
    'Categories': 'education',
    'sequence': 7,
    'summary': 'Managing school',
    'description': """
        Add student
    """,
    'website': 'https://www.quantum-space.co/',
    'depends': ['base',],
    'data': [
        #'security/hr_referral_security.xml',
    'security/ir.model.access.csv',

    'views/student_school_views.xml'
    ],
    'installable': True,
    'application': True,
}
