# -*- coding: utf-8 -*-
# © 2017 Groupe URD - Olivier Sarrat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "thundercardbook_sync",

    'summary': "Mozilla Thunderbird Cardbook addon synchronization with Odoo newsletter subscriptions.",
	
    "version": "8.0.1.0.0",

    'author': "Groupe URD",
    'website': "http://www.urd.org",
    "license": "AGPL-3",
    "application": False,
    "installable": True,

    # Categories can be used to filter modules in modules listing
    'category': 'marketing',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
}