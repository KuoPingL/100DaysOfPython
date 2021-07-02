import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("OWM_API_KEY")
auth_token = os.getenv("OWM_AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+13607955332',
                              to='+8860918756081'
                          )

print(message.body)