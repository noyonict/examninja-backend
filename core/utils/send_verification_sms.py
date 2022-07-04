from twilio.rest import Client


def send_verification_sms(phone_number, verification_code):
    account_sid = 'AC018dfdd3ae4a1b6423c7715e9bb99be3'
    auth_token = 'fa51aeb6ba148c7a885f5dd98b559c45'
    client = Client(account_sid, auth_token)
    print(phone_number)
    message = client.messages.create(
        messaging_service_sid='MGa551277654cb8c0e81e8c7ccc92ba987',
        body=f'Your verfication code for exam ninja is {verification_code}',
        to=f"+88{phone_number}"
    )
    print(message.sid)
