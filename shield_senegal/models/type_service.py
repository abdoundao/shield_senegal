from odoo import models, fields, api


class TypeService(models.Model):
    _name = 'type.service'
    _inherit = ['mail.thread']

    name = fields.Char(string="Nom", tracking=True)
    fonction_employe_line_ids = fields.One2many('fonction.employe.line', 'service_type_id', string="Type d'employés requis")
    type_materiel_ids = fields.Many2many('type.materiel', string="Types de matériel")
    product_ids = fields.Many2many('product.product', string="Produits", tracking=True)
    duration = fields.Integer(string='Durée en minutes', store=True, tracking=True)
    duration_display = fields.Char(string='Durée', compute='_compute_duration_display')

    @api.depends('duration')
    def _compute_duration_display(self):
        for record in self:
            hours = int(record.duration / 60)
            minutes = int(record.duration % 60)
            record.duration_display = '{:02d}:{:02d}'.format(hours, minutes)

