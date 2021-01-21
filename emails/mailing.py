import smtplib


PROVIDERS_ADDRESSES = {
  'gmail': 'smtp.gmail.com',
  'hotmail': 'smtp.live.com',
  'outlook': 'outlook.office365.com',
  'yahoo': 'smtp.mail.yahoo.com',
}

class EmailSender:
  def __init__(
    self,
    user,
    password,
    provider = 'gmail',
    port = 587,
  ):
    """Constructor

    Args:
        user (string): User's email address
        password (string): User's password
        provider (str, optional): Email provider. Defaults to 'gmail'.
        port (int, optional): Connection port. Defaults to 587.
    """    
    self.__user = user
    self.__password = password
    self.__provider = provider
    self.__port = port 

  def send_mail(self, email, subject, body):
    """Sends an email a destination address

    Args:
        email (string): Destination email address
        subject (string): Email subject
        body (string): Email body
    """
    provider_address = PROVIDERS_ADDRESSES[self.__provider]

    with smtplib.SMTP(provider_address, port = self.__port) as conn:
      conn.starttls()
      conn.login(user = self.__user, password = self.__password)
      conn.sendmail(
        from_addr = self.__user,
        to_addrs = email,
        msg = f'Subject:{subject}\n\n{body}',
      )

