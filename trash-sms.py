import os

from twilio.rest import Client

# Twilio Creds
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Roomie Info
numbers = {
        'John' : '+16076610544',
        'Ingrid' : '+16263288581',
        'Jack' : '+16039690268',
        'Sean James' : '+19789952266'}

for name, number in numbers.items():
    message = client.messages \
            .create(
                    body="Hi " + name + " \U0001F920 This is your friendly reminder that today is trash day!",
                    from_='+16178127055',
                    to=number
                    )
    print(message.sid)



