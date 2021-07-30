from odoo import tools
from odoo import api, fields, models


class AppointmentReport(models.Model):
    _name = "appointment.report"
    _description = "Pdf repport for appointment"
    _rec_name = "customer_name"

    customer_name = fields.Many2one('res.partner', string="Customer Name")
    age = fields.Char(string='Age')
    email_id = fields.Char(string='Email Id')
    from_date = fields.Datetime(string='From Date')
    to_date = fields.Datetime(string='To Date')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    feedback = fields.Text(string='Your Feedback')
    customer_dob = fields.Date(string='Birth Date')
    customer_image = fields.Binary(string='Image')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Approved'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, default='draft')

    # @api.model
    # def _get_done_states(self):
    #     return ['sale', 'done', 'paid']
