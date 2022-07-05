import os
from twilio.rest import Client


def send_verification_sms(phone_number, verification_code):
    account_sid = os.environ.get("ACCOUNT_SID", default="AC018dfdd...")
    auth_token = os.environ.get("AUTH_TOKEN", default="fa51aeb6ba14...")
    client = Client(account_sid, auth_token)
    print(phone_number)
    message = client.messages.create(
        messaging_service_sid=os.environ.get("MESSAGING_SERVICE_SID", default="MGa551..."),
        body=f'Your verfication code for exam ninja is {verification_code}',
        to=f"+88{phone_number}"
    )
    print(message.sid)
