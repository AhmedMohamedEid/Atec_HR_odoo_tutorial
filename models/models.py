# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class AtecEmployee(models.Model):
    _name = 'atec.employee' # Creates a table with name 'atec_employee'
    _description = 'Atec Employee'
    _inherit = ['mail.thread']

    name = fields.Char(string='Employee Name', required=True, )
    email = fields.Char(string="Email", required=True)
    marital_status = fields.Selection(string="Marital status", selection=[('m', 'Married'), ('s', 'Single')], default='s')
    birth_date = fields.Date(string="Birth Date", default=fields.Date.today, )
    website = fields.Char(string="Website", required=False, )
    phone = fields.Char(string="Phone", required=False, )
    relative_ids = fields.One2many(comodel_name="res.partner", inverse_name="atec_emp_id", string="Relatives", required=False, )
    image = fields.Binary(string="Image", attachment=True, store=True, )

    _sql_constraints = [
        ('atec_emp_unique_email', 'unique(email)', 'Emails should be unique!')
    ]

    @api.constrains('email')
    def check_email(self):
        if self.email.endswith('gmail.com'):
            raise UserError('Gmail is not accepted')

    @api.onchange('email')
    def onchange_email(self):
        if self.email and self.email.endswith('gmail.com'):
            return {
                'warning': {
                    'title': 'Wrong Email',
                    'message': 'Gmail is not accepted **'
                },
                'value': {
                    'website': 'http://%s' % self.email.split('@')[1],
                },
                # 'domain': {
                #     'FIELD_NAME': DOMAIN
                # }
            }
        if self.email:
            self.website = 'http://%s' % self.email.split('@')[1]


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    atec_emp_id = fields.Many2one(comodel_name="atec.employee", string="", required=False, )
