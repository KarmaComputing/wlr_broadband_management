# -*- coding: utf-8 -*-

from odoo import models, fields, api

class karma_wlr(models.Model):
     _name = 'karma_wlr.karma_wlr'

     lead_id = fields.Many2one('crm.lead', 
             ondelete='set null', string="Lead", index=True)
     partner_id = fields.Many2one('res.partner',
             ondelete='set null', string="Customer", index=True)
     router = fields.Char()
     ssid = fields.Char()
     wifi_password = fields.Char()
     adsl_username = fields.Char()
     adsl_password = fields.Char()
     service = fields.Many2one('product.template',
             ondelete='set null', string="Service", index=True)
     configured_modem = fields.Boolean()
     sent_modem = fields.Datetime()
     line_installed = fields.Datetime()
     confirmed_online = fields.Datetime()
     description = fields.Text()

     @api.depends('value')
     def _value_pc(self):
         self.value2 = float(self.value) / 100
