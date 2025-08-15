import requests
from datetime import datetime

# URL = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(url=URL)
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)


URL = "https://api.sunrise-sunset.org/json"

MY_LAT = 6.451140
MY_LONG = 3.388400

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(URL, parameters)
response.raise_for_status()
location = response.json()
sunrise = location["results"]["sunrise"]
sunset = location["results"]["sunset"]

print(sunrise)