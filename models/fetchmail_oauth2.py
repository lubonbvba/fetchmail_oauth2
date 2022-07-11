# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
import winrm,pdb,logging

from openerp import SUPERUSER_ID
#from openerp.osv import orm, fields
from openerp.tools.translate import _
import json
import requests, msal, base64
import imaplib

logger = logging.getLogger(__name__)


class fetchmail_server(models.Model):
    _name = "fetchmail.server"
    _inherit = "fetchmail.server"
    url=fields.Char()
    client_id=fields.Char()
    oauth2=fields.Boolean(help="When using oauth2, password is the cliet secret")

    def connect(self):
        
        if  self.oauth2:
            client_id=self.client_id
            secret=self.password
            url=self.url
            app = msal.ConfidentialClientApplication(
            client_id, authority=url,
            client_credential=secret,
            # token_cache=...  # Default cache is in memory only.
                           # You can learn how to use SerializableTokenCache from
                           # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache
            )
            result=None
            result = app.acquire_token_silent(['https://outlook.office365.com/.default'], account=None)
            if not result:
                logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
                result = app.acquire_token_for_client(scopes=['https://outlook.office365.com/.default'])

            if "access_token" in result:
                auth_string = 'user=%s\1auth=Bearer %s\1\1' % (self.user, result['access_token'])
                #text = base64.b64encode(auth_string)
            #     # Calling graph using the access token
            #     graph_data = requests.get(  # Use token to call downstream service
            #     cmd_line,
            #     headers={'Authorization': 'Bearer ' + result['access_token']}, )
            #     return graph_data.json()
                connection = imaplib.IMAP4_SSL(self.server)
                #connection.debug = 5
                connection.authenticate('XOAUTH2', lambda x: auth_string)
                #pdb.set_trace()
            else:
                print(result.get("error"))
                print(result.get("error_description"))
                print(result.get("correlation_id"))  # You may need this when reporting a bug
        else:
            connection=super(fetchmail_server, self).connect()
        return connection

    def _fetch_mails(self):
        if not ids:
            ids = self.search(cr, uid, [('state','=','done'),('type','in',['pop','imap'])])
        return self.fetch_mail(cr, uid, ids, context=context)







