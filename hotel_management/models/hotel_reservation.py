from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HotelReservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Hotel Reservation'

    guest_name = fields.Char(string="Guest Name", required=True, translate=True)
    room_id = fields.Many2one('hotel.room', string="Room", required=True)
    check_in_date = fields.Date(string="Check-In Date", required=True)
    check_out_date = fields.Date(string="Check-Out Date", required=True)
    status = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('checked_in', 'Checked In'), ('checked_out', 'Checked Out')],
        string="Status", default='draft'
    )

    @api.constrains('check_in_date', 'check_out_date')
    def _check_dates(self):
        for record in self:
            if record.check_out_date <= record.check_in_date:
                raise ValidationError("Check-out date must be after check-in date.")
