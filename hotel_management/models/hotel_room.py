from odoo import models, fields, api


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string="Room Number", required=True, translate=True)
    room_type = fields.Selection(
        [('standard', 'Standard'), ('deluxe', 'Deluxe'), ('suite', 'Suite')],
        string="Room Type", required=True
    )
    status = fields.Selection(
        [('available', 'Available'), ('occupied', 'Occupied'), ('out_of_service', 'Out of Service')],
        string="Status", default='available'
    )
    price = fields.Float(string="Price per Night")

    namee = fields.Many2one('res.partner', string="Customer Name")


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Override name_search method to include phone search
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            # Searching by name or phone number
            args += ['|', ('name', operator, name), ('phone', operator, name)]
        return super(ResPartner, self).name_search(name, args=args, operator=operator, limit=limit)
