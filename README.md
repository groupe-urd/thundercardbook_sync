# ThunderCardbook Sync
Mozilla Thunderbird Cardbook addon synchronization with Odoo newsletter subscriptions.


## Description
Works in two steps:
1. An XML-RPC service able to parse a Cardbook mailPopularityIndex.txt file and populate a subscription contact ignore list
	table specific to each Odoo user. This service will return an URL to the following form if a new contact is added to this table.
2. A web form which based on the content of the subscription contact ignore list table specific to each Odoo user, giving
	to the user the possibility to choose either to which newsletter(s) the contact can be subscribed, either to ignore this contact and
	no more ask to subscribe it to newsletters.

This Odoo module requires to have the Cardbook addon installed on the Mozilla Thunderbird side to easily collect addressbook contacts in text format.