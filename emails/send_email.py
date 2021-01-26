import os, sys; 
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.dirname(current_dir))

from core.mailing import EmailSender

sender = EmailSender(
  os.getenv('USERNAME'),
  os.getenv('PASSWORD'),
)

sender.send_mail(
  'john@foo.com',
  'Hello',
  'Hello my friend',
)
