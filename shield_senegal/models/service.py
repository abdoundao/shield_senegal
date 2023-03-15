from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Service(models.Model):

    _inherit = ['mail.thread']

    _name = 'service'
    name = fields.Char(string='Nom', required=True,
                              default=lambda self: self.env['ir.sequence'].next_by_code('service.seq'), readonly=1)
    partner_id = fields.Many2one('res.partner', string="Client", required=1, tracking=True)
    employe_ids = fields.Many2many('employe', string="Employé")
    materiel_ids = fields.Many2many('materiel', string="Matériel")
    type_service_id = fields.Many2one('type.service', string="Type de service", tracking=True)
    product_ids = fields.Many2many('product.product', string="Produits")
    comment = fields.Text("Commentaire", tracking=True)
    service_datetime_begin = fields.Datetime('Date de la prestation',
                                       default=lambda self: fields.Datetime.now(), tracking=True)
    service_datetime_end = fields.Datetime("Date de fin de prestation", tracking=True)
    state = fields.Selection([
        ('non_effectue', 'Non effectué'),
        ('annule', 'Annulé'),
        ('en_attente_confirmation', 'En attente de confirmation'),
        ('en_cours', 'En cours'),
        ('effectue', 'Effectué'),
    ], string='État', default='en_attente_confirmation')

    @api.onchange('service_datetime_begin')
    def _onchange_service_datetime_begin(self):
        self.ensure_one()
        if self.type_service_id.duration and self.service_datetime_begin:
            duration = self.type_service_id.duration
            self.service_datetime_end = self.service_datetime_begin + relativedelta(minutes=duration)


