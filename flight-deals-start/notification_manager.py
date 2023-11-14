import requests
from twilio.rest import Client

account_sid = "AC1d16cd6bc0bcb27223af3e0c029f03c7"
auth_token = "1be827d8cd80bb8d4124748deeed36bc"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_alert(self, flight_details, sheet_data):
        for flight_data in sheet_data:
            if flight_details['ACN'] == flight_data['city'] and flight_details['price'] < flight_data['lowestPrice']:
                body = f"Low price alert! Only £{flight_details['price']} to fly from {flight_details['DCN']}" \
                       f"-{flight_details['DAIC']} to {flight_details['ACN']}" \
                       f"-{flight_details['AAIC']} from {flight_details['outbound']} to {flight_details['inbound']}"

                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body=body,
                    from_='+1 507 353 4477',
                    to='+233 553405536'
                )

                print(message.sid)
