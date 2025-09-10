from data_manager import DataManager
from flight_search import FlightSearch
import requests
import json


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.




# Create an object instance of DataManager
city_data = DataManager()
# Create an object instance of FlightSearch
flight_data = FlightSearch()


# Get all city names from Google Sheet
cities = city_data.get_cities()



# Authenticate Amadeus
flight_data.get_flight_offers()

print(flight_data.get_token())
print(flight_data.get_flight_offers())


# Get IATA codes for each city

iata_Code = []

for city in cities:
    flight_data.get_flight_offers(city)
    print(iata_Code)

id_range = range(2, 11, 1)

ObjectID = []


def add_iataCode():
    for id in id_range:
        global ObjectID
        ObjectID = id

        # print(ObjectID)
        code = (iata_Code[id])

        body = {
            "price": {
                "iataCode": code
            }
        }

        url = f"https://api.sheety.co/42901ff3c79bd4dcb77433f745c52d28/flightDeals/prices/{ObjectID}"
        response = requests.put(url=url, json=body)
        print(f"Updating row {ObjectID} with code {code}")
        print(response.text)


def get_details():
    url = "https://api.sheety.co/42901ff3c79bd4dcb77433f745c52d28/flightDeals/prices"
    response = requests.get(url=url)
    data = json.dumps(response.json(), indent=4)
    print(data)

add_iataCode()
#get_details()