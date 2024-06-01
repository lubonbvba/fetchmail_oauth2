# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions
import pdb,logging

from openerp import SUPERUSER_ID
#from openerp.osv import orm, fields
#from openerp.tools.translate import _
import json
import requests, base64
import imaplib
import openerp.tools as tools
import re

logger = logging.getLogger(__name__)

address_pattern = re.compile(r'([^ ,<@]+@[^> ,]+)')

def try_coerce_ascii(string_utf8):
    """Attempts to decode the given utf8-encoded string
       as ASCII after coercing it to UTF-8, then return
       the confirmed 7-bit ASCII string.

       If the process fails (because the string
       contains non-ASCII characters) returns ``None``.
    """
    try:
        string_utf8.decode('ascii')
    except UnicodeDecodeError:
        return
    return string_utf8

def extract_rfc2822_addresses(text):
    """Returns a list of valid RFC2822 addresses
       that can be found in ``source``, ignoring 
       malformed ones and non-ASCII ones.
    """
    if not text: return []
    candidates = address_pattern.findall(tools.ustr(text).encode('utf-8'))
    return filter(try_coerce_ascii, candidates)


class ir_mail_server(models.Model):
    _name = "ir.mail_server"
    _inherit = "ir.mail_server"
    
    
    def build_email(self, email_from, email_to, subject, body, email_cc=None, email_bcc=None, reply_to=False,
               attachments=None, message_id=None, references=None, object_id=False, subtype='plain', headers=None,
               body_alternative=None, subtype_alternative='plain'):
          
          defaultdomain=tools.config.get('mail_domain')
          defaultfrom=tools.config.get('mail_from')
          adress=extract_rfc2822_addresses(email_from)
          adress=adress[-1]
          domain=adress[adress.index('@')+1:]
          if domain != defaultdomain:
              newfrom=email_from.replace(adress,defaultfrom)
              logger.info('ir_mail_server_b: newfrom: %s', newfrom)
              email_from=newfrom

          
          logger.info('ir_mail_server_b: Email_from: %s', email_from)
          logger.info('ir_mail_server_b: used e-mailaddress: %s, domain=%s', adress,domain)
          logger.info('ir_mail_server_b: Default domain: %s', defaultdomain)

          
          
          msg=super(ir_mail_server, self).build_email( email_from, email_to, subject, body, email_cc, email_bcc, reply_to,
               attachments, message_id, references, object_id, subtype, headers,
               body_alternative, subtype_alternative='plain')
          
          return msg