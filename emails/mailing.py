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
    self.__user = user
    self.__password = password
    self.__connection = smtplib.SMTP(PROVIDERS_ADDRESSES[provider], port = port)

  def send_mail(self, email, message):
    conn = self.__connection
    conn.starttls()
    conn.login(user = self.__user, password = self.__password)
    conn.sendmail(
      from_addr = self.__user,
      to_addr = email,
      msg = message,
    )
    conn.close()

