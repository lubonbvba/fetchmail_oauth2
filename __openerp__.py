# -*- coding: utf-8 -*-
{
    'name': "fetchmail_oauth2",

    'summary': """
        Implement oauth2 login for imap""",

    'description': """
    Check https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth
    for the creation of an Application
    \nFollow the Use client credentials grant flow to authenticate IMAP and POP connections
    \n
    \n Module also contains a fix to set the mailfrom on outgoing e-mails in case it is different from the address specfied in config file
    \n mail_domain=default outgoing domain
    \n mail_from=address to be used in case the outgoing domain is different from mail_domain
    """,

    'author': "Lubon bvba",
    'website': "http://www.lubon.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.9',

    # any module necessary for this one to work correctly
    'depends': ['base','fetchmail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
        'views/fetchmail_oauth2.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
