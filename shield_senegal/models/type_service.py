from odoo import models, fields, api


class TypeService(models.Model):
    _name = 'type.service'
    _inherit = ['mail.thread']

    name = fields.Char(string="Nom", tracking=True)

