from odoo import models, fields


class HousekeepingTask(models.Model):
    _name = 'housekeeping.task'
    _description = 'Housekeeping Task'

    name = fields.Char(string="Task Name", required=True)
    room_id = fields.Many2one('hotel.room', string="Room", required=True)
    task_type = fields.Selection(
        [('cleaning', 'Cleaning'), ('maintenance', 'Maintenance')],
        string="Task Type", required=True
    )
    status = fields.Selection(
        [('pending', 'Pending'), ('in_progress', 'In Progress'), ('done', 'Done')],
        string="Status", default='pending'
    )
