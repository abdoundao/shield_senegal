from odoo import models, fields

class GeoZone(models.Model):

    _inherit = ['mail.thread']
    _name = 'geo.zone'
    name = fields.Char(string="Nom", tracking=True)
