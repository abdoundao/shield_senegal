from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError


class Employe(models.Model):
    _inherit = ['mail.thread']

    _name = 'employe'
    name = fields.Char(string="Nom", tracking=True)
    prenom = fields.Char(string="Prénom", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    phone = fields.Char(string="Numéro de téléphone", tracking=True)
    code = fields.Char(string="Code", size=10, required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('employe.code'), tracking=True)
    fonction_employe_id = fields.Many2one('fonction.employe', string="Fonction", tracking=True)

    @api.constrains('email')
    def _check_email_format(self):
        for employee in self:
            if employee.email and not re.match(r"[^@]+@[^@]+\.[^@]+", employee.email):
                raise ValidationError("Le format de l'adresse email est invalide !")

    def name_get(self):
        return [(record.id, "%s-%s %s" % (record.code, record.name, record.prenom)) for record in self]
