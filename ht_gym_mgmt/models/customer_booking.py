from odoo import api,fields, models,_
from datetime import date, datetime
from odoo.exceptions import UserError, ValidationError

class Membership(models.Model):
    _name = 'customer.booking'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Name')
    email = fields.Char(related='partner_id' ,string='Email Id')
    mobile = fields.Char(related='partner_id', string='Mobile')
    is_membership = fields.Boolean(string='Membership ?')
    membership = fields.Many2one('customer.membership',string='Membership')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    price = fields.Float(string='Price')
    shift = fields.Selection([('morning','Morning'),('evening','Evening')],string='Shift')
    workout_hour = fields.Float(string='Workout Time')
    purpose = fields.Selection([('general','General Fitness'),('weightloss','Weight Loss'),('tournament','Tournament')],string='Purpose')
    month_year = fields.Selection([('month','Month'),('year','Year')])
    duration = fields.Integer(string='Duration')