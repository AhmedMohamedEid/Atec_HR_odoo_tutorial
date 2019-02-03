# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AtecEmployee(models.Model):
    _name = 'atec.employee' # Creates a table with name 'atec_employee'
    _description = 'Atec Employee'
    _inherit = ['mail.thread']

    name = fields.Char(string='Employee Name', required=True, )
    email = fields.Char(string="Email", required=True)
    marital_status = fields.Selection(string="Marital status", selection=[('m', 'Married'), ('s', 'Single')], default='s')