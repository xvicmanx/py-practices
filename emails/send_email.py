from mailing import EmailSender

sender = EmailSender(
  'user',
  'pass',
)

sender.send_mail('john@foo.com', 'Hello')
