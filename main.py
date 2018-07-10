from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

import auth

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)


import send_email

sendInst = send_email.send_email(service)
message = sendInst.create_message('ivvraghavendra1999@gmail.com','123456sasank@gmail.com', 'Hello_API','Hello this is testing Mail')
sendInst.send_message('me',message)
