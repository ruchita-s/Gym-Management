from odoo import api,fields, models,_
from datetime import date, datetime
from odoo.exceptions import UserError, ValidationError

class Membership(models.Model):
    _name = 'customer.booking'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Name')
    email = fields.Char(string='Email Id',related='partner_id.email')
    mobile = fields.Char(string='Mobile',related='partner_id.mobile')
    is_membership = fields.Boolean(string='Membership?')
    membership = fields.Many2one('customer.membership',string='Membership')
    start_date = fields.Datetime(string='Start Date')
    end_date = fields.Datetime(string='End Date')
    price = fields.Float(string='Price', related='membership.price')
    shift = fields.Selection([('morning','Morning'),('evening','Evening')],string='Shift')
    workout_hour = fields.Float(string='Workout Time')
    purpose = fields.Selection([('general','General Fitness'),('weightloss','Weight Loss'),('tournament','Tournament')],string='Purpose',related='membership.purpose')
    month_year = fields.Selection([('month','Month'),('year','Year')],string='Type')
    duration = fields.Integer(string='Duration')
    date = date.today()

    @api.onchange('membership')
    def get_end_date(self):
        chk_type = self.env['customer.membership'].search([('name','=',self.membership.name)])
        print("...........in the loop..........................",chk_type)
        get_type = chk_type.membership
        print(".........get_type...............",get_type)
        get_duration = chk_type.duration
        print("............duration...............",get_duration)
        
        if chk_type.membership == 'month':
            print("..........current month............",self.date)
            # month = date.today().strftime('%B')
            # my_months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
            # calculation = month[my_months] + chk_type.duration
            # print("....................calculation...........................",calculation) 
            date_1= (datetime.strptime(self.date, '%Y-%m-%d')+relativedelta(days =+ 42)) 
            print("....................date_1......................",date_1)           








