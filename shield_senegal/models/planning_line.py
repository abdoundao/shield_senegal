from odoo import models, fields

class PlanningLine(models.Model):
    _name = 'planning.line'
    _description = 'Planning Line'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    start_date = fields.Datetime(string='Date de début', required=True)
    end_date = fields.Datetime(string='Date de fin', required=True)
    service_id = fields.Many2one('service', string='Service')
    is_leave = fields.Boolean(string='Est un congé', default=False)
    vis_name = fields.Char("Nom Affiché", compute='compute_vis_name')

    def compute_vis_name(self):
        for rec in self:
            if rec.is_leave:
                rec.vis_name = "Congé"
            elif rec.service_id.name:
                rec.vis_name = rec.service_id.name
            else:
                rec.vis_name = "Prestations"