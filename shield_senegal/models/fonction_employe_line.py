from odoo import models, fields


class FonctionEmployeLine(models.Model):
    _inherit = ['mail.thread']
    _name = 'fonction.employe.line'

    number = fields.Integer(string="Nombre")
    fonction_employe_id = fields.Many2one('hr.job', string="Fonctions employés")
    service_id = fields.Many2one('service', string="service")