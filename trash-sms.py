import os
import sys
import requests
import random
from twilio.rest import Client
from datetime import date, timedelta
today = date.today()


# Twilio Creds
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Joke
response = requests.get('https://icanhazdadjoke.com', headers={"Accept":"text/plain"})
if response.status_code != 200:
    joke = "How does Moses make his cup of tea? Hebrews it";
else:
    joke = response.content.decode('utf-8')

# Holidays
holidays = { date(month=9,day=2,year=2019): True,
            date(month=10, day=14,year = 2019):True,
            date(month=11, day=11,year = 2019):True,
            date(month=11, day=28,year = 2019):True,
            date(month=11, day=29,year = 2019):True,
            date(month=12, day=24,year = 2019):True,
            date(month=12, day=25,year = 2019):True}

messages = [" \U0001F920 This is your friendly reminder that the trash needs assistance getting to the curb today!",
            " \U0001F920 We need to talk. About trash. It needs to go out today \U0001F5D1",
            " \U0001F920 Hope you are have a lovely trash day \U0001F618!",
            " \U0001F920! Happy Trash Day! To celebrate, here is a joke: " + joke,
            " \U0001F920 " + joke + " Oh, and it's trash day. ",
            " \U0001F920! Oh, I love trash! Anything dirty or dingy or dusty! Anything ragged or rotten or rusty! Yes, I love trash!",
            " \U0001F920! Unfortunately, we don't have the Sean James Trash Co. yet, so we still gotta take out the trash. ",
            " \U0001F920 Just because you're trash doesn't mean you can't do great things. It is called garbage can, not garbage cannot. ",
            " \U0001F920 There is no such thing as garbage, just useful stuff in the wrong place. Except the garbage we need to take out, that is garbage.",
            " \U0001F920 I don't talk trash often, but when I do, I tell you to take it out.",
            " \U0001F920 I'm thinking of being a joke bot instead of a trash bot, here's a new one: " + joke,
            ]

# Roomie Info
numbers = {
        'name':'+phone_number',
        'name2': '+phone_number'
        }

holiday = False
for i in range(-4,1):
    if holidays.get(today + timedelta(days=i)) is True:
        holiday = True;

day = sys.argv[1];


if((day == "thu" and holiday)):
    for name, number in numbers.items():

        message = client.messages \
            .create(
                    body="Hi " + name + "! We had a holiday, no trash today \uE312\uE312!",
                    from_='twilio_phone_number',
                    to=number
                    )
        print(message.sid)


if((day == "thu" and not holiday) or (day == "fri" and holiday)):
    rand = random.randint(0,len(messages)- 1)
    for name, number in numbers.items():
        message = client.messages \
            .create(
                    body="Hi " + name + messages[rand],
                    from_='+twilio_phone_number',
                    to=number
                    )
        print(message.sid)

