# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
import pdb,logging

from openerp import SUPERUSER_ID
#from openerp.osv import orm, fields
#from openerp.tools.translate import _
import json
import requests, base64
import imaplib

logger = logging.getLogger(__name__)

class ir_mail_server(models.Model):
    _name = "ir.mail_server"
    _inherit = "ir.mail_server"
    
    
    def build_email(self, email_from, email_to, subject, body, email_cc=None, email_bcc=None, reply_to=False,
               attachments=None, message_id=None, references=None, object_id=False, subtype='plain', headers=None,
               body_alternative=None, subtype_alternative='plain'):
          logger.info('ir_mail_server_b: Email_from: %s', email_from)
          msg=super(ir_mail_server, self).build_email( email_from, email_to, subject, body, email_cc, email_bcc, reply_to,
               attachments, message_id, references, object_id, subtype, headers,
               body_alternative, subtype_alternative='plain')
          #pdb.set_trace()
          return msg