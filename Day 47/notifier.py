from twilio.rest import Client
import os
from item_price import PriceTag



class SendMail(PriceTag):

    def __init__(self, get_price):
        super().__init__() 
        self.account_sid = os.environ.get("TWILIO_ACC_SID")
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
        self.price = get_price


    def push_notification(self): # method to send sms notiticatiob
        if self.price < 100.00:
            # Create a Twilio client
            message = self.client.messages.create(
                body=f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart is now {self.price} \n https://appbrewery.github.io/instant_pot/",
                from_="+18145645908",
                to="+2348025959940",
            )
            print(message.status)



