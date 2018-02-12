# -*- coding: utf-8 -*-
from openerp import tools
from openerp import http
from openerp.http import request
from openerp import models, fields, api, _

import pprint


class ThundercardbookSync(http.Controller):
	@http.route('/thundercardbook_sync/subscriptions_form_user<user_id>', auth='user', website=True) #website=True parameter compulsory to have a website layout
	def display_subscriptions_form(self, user_id, db):
		http.request.session.db = db
		user = http.request.env['res.users'].search([('id','=',user_id)])
		
		# Read the content of the subscription_ignore_list table
		subscription_ignore_list = http.request.env['thundercardbook_sync.subscription_ignore_list'].search([
																										('user_id','=',int(user_id)),
																										('ignore','=',False)
																									])
		mass_mailing_lists = http.request.env['mail.mass_mailing.list'].search([])
		
		# Display the form based on the content of the subscription_ignore_list table
		return request.website.render("thundercardbook_sync.subscriptions_list", {'user': user, 
			'subscription_ignore_list': subscription_ignore_list,
			'mass_mailing_lists': mass_mailing_lists})
	
	
	@http.route('/thundercardbook_sync/subscribe_contacts', auth='user', website=True, methods=['POST'])
	def subscribe_contacts(self, **kwargs):
		mass_mailing_lists = http.request.env['mail.mass_mailing.list'].search([])
		# for mailing_list in mass_mailing_lists:
			# print request.form.getlist("subscribeTo%s[]" % mailing_list.id)
		for param in request.params:
			if param.startswith('subscribe'):
				subparamsArray = param.split('_')
				print "subscribe contact %s to mailing list %s" % (subparamsArray[1],subparamsArray[3])
				# Subscribe contact
				contact = http.request.env['thundercardbook_sync.subscription_ignore_list'].search([('id','=',int(subparamsArray[1]))])
				http.request.env['mail.mass_mailing.contact'].create([{'list_id': int(subparamsArray[3]), # TODO reprendre ici en mettant un "vals" au format dictionnaire comme [(6,False,team_ids_vals)]
																	'email': contact.email}]
																	)
			if param.startswith('ignore'):
				subparamsArray = param.split('_')
				print "ignore contact %s" % subparamsArray[1]
		return "OK"