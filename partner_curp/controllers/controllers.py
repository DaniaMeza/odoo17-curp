# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerCurp/odoo17(http.Controller):
#     @http.route('/partner_curp/odoo17/partner_curp/odoo17', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_curp/odoo17/partner_curp/odoo17/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_curp/odoo17.listing', {
#             'root': '/partner_curp/odoo17/partner_curp/odoo17',
#             'objects': http.request.env['partner_curp/odoo17.partner_curp/odoo17'].search([]),
#         })

#     @http.route('/partner_curp/odoo17/partner_curp/odoo17/objects/<model("partner_curp/odoo17.partner_curp/odoo17"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_curp/odoo17.object', {
#             'object': obj
#         })

