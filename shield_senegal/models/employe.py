from odoo import models, fields


class EmployeeInherited(models.Model):
    _inherit = 'hr.employee'

    geo_zone_ids = fields.Many2many('geo.zone', string='Zones Géographiques')
