from odoo import models, fields


class FonctionEmploye(models.Model):
    _inherit = ['mail.thread']

    _name = 'fonction.employe'
    name = fields.Char(string="Nom", tracking=True)

