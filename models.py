# -*- coding: utf-8 -*-

from openerp import models, fields, api

class thundercardbook_sync(models.Model):
	_name = 'thundercardbook_sync.subscription_ignore_list'

	email = fields.Text(string="Email", translate=True)
	user_id = fields.Many2one("res.users", string="User")
	ignore = fields.Boolean("Ignore", default=False)
	popularity = fields.Integer('Popularity')        
	
	#Parse a Thunderbird Cardbook mailPopularityIndex.txt
	@api.model
	def parse_subscription_list(self, user_id, data_file):
		if not self.env['res.users'].search([('id','=',user_id)]):
		    raise Exception('User %d not exist !')
		contact_list = self.search([('user_id','=',user_id)])
		email_contact_list = [contact.email for contact in contact_list]
		data_file_array = data_file.split('\n')
		for line in data_file_array:
			email = line.split(':')[0]
			popularity = line.split(':')[1]
			if email not in email_contact_list:
				self.create({'email': email,'user_id': user_id, 'popularity': popularity})
		return "/thundercardbook_sync/subscriptions_form_user%s" % user_id
		