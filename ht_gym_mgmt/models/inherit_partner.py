from odoo import api,fields, models,_

class ResPartner(models.Model):
    _inherit = 'res.partner'

    member_type = fields.Selection([('trainee','Trainee'),('coach','Coach')])
