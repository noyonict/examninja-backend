from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


def send_verification_sms(phone_number, verification_code):
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    print(phone_number)
    message = client.messages.create(
        from_="Exam Ninja",
        messaging_service_sid=os.getenv("MESSAGING_SERVICE_SID"),
        body=f'Your verfication code for exam ninja is {verification_code}',
        to=f"+88{phone_number}"
    )
    print(message.sid)

    
