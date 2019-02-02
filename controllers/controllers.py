# -*- coding: utf-8 -*-
from odoo import http

# class AtecHr(http.Controller):
#     @http.route('/atec_hr/atec_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/atec_hr/atec_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('atec_hr.listing', {
#             'root': '/atec_hr/atec_hr',
#             'objects': http.request.env['atec_hr.atec_hr'].search([]),
#         })

#     @http.route('/atec_hr/atec_hr/objects/<model("atec_hr.atec_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('atec_hr.object', {
#             'object': obj
#         })