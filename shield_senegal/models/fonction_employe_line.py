from odoo import models, fields


class FonctionEmployeLine(models.Model):
    _inherit = ['mail.thread']
    _name = 'fonction.employe.line'

    number = fields.Integer(string="Nombre")
    fonction_employe_id = fields.Many2one('fonction.employe', string="Fonctions employés")
    service_type_id = fields.Many2one('type.service', string="Type de service")