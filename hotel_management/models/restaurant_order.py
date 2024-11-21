from odoo import models, fields, api


class RestaurantOrder(models.Model):
    _name = "restaurant.order"
    _description = "Restaurant Order"

    table_number = fields.Char(string="Table Number", required=True)
    order_date = fields.Datetime(string="Order Date", default=fields.Datetime.now, required=True)
    total_amount = fields.Float(string="Total Amount", compute="_compute_total_amount", store=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
    ], default='draft', string="Status", required=True)
    order_line_ids = fields.One2many('restaurant.order.line', 'order_id', string="Order Lines")

    @api.depends('order_line_ids.subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.subtotal for line in order.order_line_ids)


class RestaurantOrderLine(models.Model):
    _name = "restaurant.order.line"
    _description = "Restaurant Order Line"

    product_id = fields.Many2one('product.product', string="Product", required=True)
    quantity = fields.Float(string="Quantity", default=1.0, required=True)
    price_unit = fields.Float(string="Unit Price", required=True)
    subtotal = fields.Float(string="Subtotal", compute="_compute_subtotal", store=True)
    order_id = fields.Many2one('restaurant.order', string="Order", ondelete="cascade")

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit
