import requests
import json
from twilio.rest import Client
import os



account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# api_key = "f69a41c9526f8b94413048c313b81962"
#
# # Define the endpoint for the weather api
# URL = "https://api.openweathermap.org/data/2.5/weather"
#
# # Define tha required parameters
# parameter = {
#     "q": "Lagos",
#     "appid": api_key
# }
#
# # Calling the endpoint to get the weather data
# response = requests.get(URL, parameter)
#
# # pretty-print JSON
# json_data = json.dumps(response.json(), indent=4)
#
# print(json_data)



#================================= Call 5 day / 3 hour forecast data ==================================================
# Weather Map API credentials
api_key = os.environ.get("OWM_API_KEY")

URL = "https://api.openweathermap.org/data/2.5/forecast"

# Define tha required parameters
parameter = {
    "lat": "11.712311",
    "lon": "11.081414",
    "cnt": 4,
    "appid": api_key
}

# Calling the api wth the required parameters
response = requests.get(URL, parameter)
response.raise_for_status()
data = response.json()


will_rain = False
for forecast in data["list"]:
    weather_id = forecast["weather"][0]["id"]
    weather_description = forecast["weather"][0]["description"]
    weather_report = (weather_id, weather_description)
    # print(weather_report)
    if weather_id < 700:
        will_rain = True

if will_rain:
    # Create a Twilio client
    client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It's going to rain today. Remember to bring an umbrella.",
    #     from_="+18145645908",
    #     to="+2348025959940",
    # )
    # print(message.status)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's time to take a nap",
        to='whatsapp:+2348025959940'
    )

    print(message.status)



