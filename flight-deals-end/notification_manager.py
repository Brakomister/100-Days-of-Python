from twilio.rest import Client
import smtplib

TWILIO_SID = "AC1d16cd6bc0bcb27223af3e0c029f03c7"
TWILIO_AUTH_TOKEN = "1be827d8cd80bb8d4124748deeed36bc"
TWILIO_VIRTUAL_NUMBER = '+1 507 353 4477'
TWILIO_VERIFIED_NUMBER = '+233 553405536'
my_email = "kbrako.asante@gmail.com"
password = "kkinywldxwhaaikt"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.connection = smtplib.SMTP("smtp.gmail.com")
        self.connection.starttls()

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, email, message):
        self.connection.login(user=my_email, password=password)
        self.connection.sendmail(to_addrs=email, from_addr=my_email, msg=message)
