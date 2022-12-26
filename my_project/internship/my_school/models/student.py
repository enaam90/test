# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class studentschool(models.Model):
    _name = 'student.school'
    _description = 'student'

    name= fields.Char(string='name', required=True, translate=True)
    birthday_date= fields.Date(string ='birthday_date', default= lambda self: fields.date.today())
    semster_fees= fields.Float(string='semster_fees',digit=(2,3))
    nationalty= fields.Many2one(string= 'res.country','nationalty',)
    gender= fields.Selection([('male', 'Male'),
                        ('femele', 'Famele')], 
                            string="Gender")
    active = fields.Boolean(string ='Active', default=True)
