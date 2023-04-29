from odoo import models, fields


class PlanningCreationWizard(models.TransientModel):
    _name = 'wizard.planning'
    _description = 'Planning Creation Wizard'

    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    employes_ids = fields.Many2many('hr.employee', string="employés")

    def create_planning(self):
        line_ids = []
        for employe in self.employes_ids:
            line_created = self.env['planning.line'].create({
                'start_date': self.start_date,
                'end_date': self.end_date,
                'employee_id': employe.id,
                'is_leave': False,
            })
            line_ids.append(line_created.id)
        return {
            'name': 'Planning',
            'view_mode': 'tree',
            'res_model': 'planning.line',
            'type': 'ir.actions.act_window',
            'domain': [
                ('id', 'in', line_ids),
            ],
        }