# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title',help="This is the title of the book", required=True, translate=True)
    code = fields.Char('code', size=40,)
    date_publish = fields.Date('Publishing Date', required=True, default= lambda self: fields.date.today())
    note = fields.Text('Internal Note')
    description = fields.Html('Description')
    state = fields.Selection([('draft', 'Not Available'),
                              ('available', 'Available'),
                              ('borrow', 'Borrowed'),
                              ('lost', 'Lost')], 'Status', default='available',readonly=False)
    pages = fields.Integer('Number Of Pages', states={'draft': [('readonly', True)]})
    rating = fields.Float('Readers Rating')
    last_update = fields.Datetime('Last Updating Date')
    publisher_id = fields.Many2one('res.partner', 'Publisher',)
    active = fields.Boolean('Active', default=True)
    reviewer_ids = fields.Many2many('res.partner', 'book_reviewer_rel', 'book_id', 'reviewer_id', 'Reviewers')
    edition_ids = fields.One2many('library.book.edition', 'book_id', 'Book Editions')
    num_of_editions = fields.Integer('Number Of Editions', compute='_compute_editions')
    _sql_constraints = [('name_unq', 'unique(code)', 'Book Title should be unique')]
    


    @api.constrains('date_publish')
    def check_publishing_date(self):
        for rec in self:
            if rec.date_publish > fields.Date.today():
                raise models.ValidationError('Publishing Date can not be in the future')

    @api.depends('edition_ids')
    def _compute_editions(self):
        for rec in self:
            rec.num_of_editions = len(rec.edition_ids)




class LibraryBookEdition(models.Model):
    _name = "library.book.edition"
    _description = "Book Editions"

    book_id = fields.Many2one('library.book', 'Book')
    book_code = fields.Char('Book Code', related='book_id.code')
    date_publish = fields.Date('Edition Date')
    edition_number = fields.Char('Edition Number', size=40)


