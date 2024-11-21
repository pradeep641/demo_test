from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date(string="Date of Birth")
