from odoo import api,fields, models,_
from odoo.exceptions import UserError, ValidationError

class Membership(models.Model):
    _name = 'customer.membership'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    membership = fields.Selection([('month','Month'),('year','Year')],string='Membership', required=True)
    duration = fields.Integer(string='Duration')
    description = fields.Text(string='Description for the Membership')
    purpose = fields.Selection([('general','General Fitness'),('weightloss','Weight Loss'),('tournament','Tournament')],string='Purpose')
    coach = fields.Boolean(string='Coach?')
    coach_id = fields.Many2one('hr.employee', string='Coach')
    price = fields.Float(string='Price')
    image = fields.Binary(string='Image')
    active = fields.Boolean(string='Active')

    @api.constrains('membership')
    def CheckMonth(self):
        for rec in self:
            if (self.membership == 'month' and self.duration > 12):
                raise ValidationError(_('Please choose Year for duration'))
