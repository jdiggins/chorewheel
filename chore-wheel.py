import sys
import os
from twilio.rest import Client

# Chore Wheel State File
state_file = '/root/roomie-app/chore-wheel.state'

# Twilio Creds
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
twilio_phone_number='+11223344'

people = [ 'Henry', 'John', 'Ingrid', 'Sean', 'Jack' ]
chores = [ 'Kitchen', 'Basement', 'Deep Clean', 'Trash Master', 'Bathroom' ]
day = sys.argv[1]
# Roomie Info
numbers = {
        'name1' : '+1234567890',
        'name2' : '+9876543210'
        }

with open (state_file, 'r') as f:
    line = f.read()
    is_turn_week = True if int(line[0]) == 1 else False
    start_person = int(line[2])

    # Logic to match person with chore
    
    send_message = False

    if (day == 'sun' and is_turn_week):
        send_message = True
        content = "Oh how the chore wheel has churned \U0001F649 \n"
        for i in range(0, 5):
            content += str.format("%s %s\n" % (people[(i + start_person) % 5] + " -- ", chores[i]))
        content += "Chores are due this coming Sunday!"
    elif (day == 'sat' and not is_turn_week):
        send_message = True
        content = "Reminder that chores are due tomorrow \U0001F64A"

    # Create message and send
    if send_message:
        for name, number in numbers.items():
            message = client.messages \
                    .create(
                        body=content,
                        from_=twilio_phone_number,
                        to=number
                        )
            print(message.sid)

    # Update chore wheel state for next week
with open(state_file, 'w') as f:
    if (day == 'sun' and is_turn_week):
        start_person = (start_person + 1) % 5


    is_turn_week = 0 if is_turn_week else 1

    line = str(is_turn_week) + ' ' + str(start_person)
    f.write(line)
