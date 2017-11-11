# -*- coding: utf-8 -*-
from odoo import http

class KarmaWlr(http.Controller):
     @http.route('/karma_wlr/karma_wlr/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/example', type='http', auth='public', website=True)
     def render_example_page(self):
         return http.request.render('karma_wlr.example_page', {})

     @http.route('/example/detail', type="http", website=True)
     def navigate_to_detail_page(self):
         # This will get all company details (in case of multicompany these are multiple records)
         companies = http.request.env['res.company'].sudo().search([])
         return http.request.render('karma_wlr.detail_page', {
         # pass company details to the webpage in a variable 
         'companies': companies
         })

     @http.route('/karma_wlr/karma_wlr/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('karma_wlr.listing', {
             'root': '/karma_wlr/karma_wlr',
             'objects': http.request.env['karma_wlr.karma_wlr'].search([]),
         })

     @http.route('/karma_wlr/karma_wlr/objects/<model("karma_wlr.karma_wlr"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('karma_wlr.object', {
             'object': obj
         })

