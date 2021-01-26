import os
from dotenv import load_dotenv
from mailing import EmailSender

load_dotenv()

sender = EmailSender(
  os.getenv('USERNAME'),
  os.getenv('PASSWORD'),
)

sender.send_mail(
  'john@foo.com',
  'Hello',
  'Hello my friend',
)
