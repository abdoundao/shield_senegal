from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Service(models.Model):

    _inherit = ['mail.thread']

    _name = 'service'
    name = fields.Char(string='Nom', required=True,
                              default=lambda self: self.env['ir.sequence'].next_by_code('service.seq'), readonly=1)
    partner_id = fields.Many2one('res.partner', string="Client", required=1, tracking=True)
    employe_ids = fields.Many2many('hr.employee', string="Employés")
    type_service_id = fields.Many2one('type.service', string="Type de service", tracking=True)
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
    fonction_employe_line_ids = fields.One2many('fonction.employe.line', 'service_id', string="Type d'employés requis")
    zone_id = fields.Many2one('geo.zone', string="Zone géographiques")




