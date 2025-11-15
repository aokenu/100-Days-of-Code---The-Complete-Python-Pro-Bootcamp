from twilio.rest import Client
import os
from item_price import PriceTag



class SendMail(PriceTag):

    def __init__(self):
        super().__init__

account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")






if will_rain:
    # Create a Twilio client
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+18145645908",
        to="+2348025959940",
    )
    print(message.status)




