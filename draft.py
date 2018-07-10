from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def create_message(sender, to, subject, message_text):

  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string())}
  def create_draft(service, user_id, message_body):

      try:
          
    message = {'message': message_body}
    draft = service.users().drafts().create(userId=user_id, body=message).execute()

    print 'Draft id: %s\nDraft message: %s' % (draft['id'], draft['message'])

    return draft
  except errors.HttpError, error:
    print 'An error occurred: %s' % error
    return None
