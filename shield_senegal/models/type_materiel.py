from odoo import models, fields


class TypeMateriel(models.Model):
    _inherit = ['mail.thread']


    _name = 'type.materiel'
    name = fields.Char(string="Nom", tracking=True)