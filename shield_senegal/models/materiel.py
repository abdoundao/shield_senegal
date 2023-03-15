from odoo import models, fields

class Materiel(models.Model):

    _inherit = ['mail.thread']
    _name = 'materiel'
    name = fields.Char(string="Nom", tracking=True)
    code = fields.Char(string="Code", size=5, required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('materiel.code'))
    type_materiel_id = fields.Many2one('type.materiel', string="Type de matériel",  tracking=True)