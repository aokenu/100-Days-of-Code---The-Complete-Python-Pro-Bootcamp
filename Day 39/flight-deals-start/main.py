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

iata_codes = []

for city in cities:
    code = flight_data.get_flight_offers(city)
    iata_codes.append(code)

id_range = range(2, 11, 1)

ObjectID = []


# Update Google Sheet with IATA codes
def add_iata_codes():
    for idx, code in enumerate(iata_codes, start=2):
        # handle empty or list values
        if isinstance(code, list):
            code = code[0] if code else ""  # take the first element or empty string

        body = {
            "price": {
                "iataCode": code
            }
        }

        url = f"https://api.sheety.co/42901ff3c79bd4dcb77433f745c52d28/flightDeals/prices/{idx}"
        response = requests.put(url=url, json=body)
        print(f"Updating row {idx} with code {code}")
        print(response.text)


def get_details():
    url = "https://api.sheety.co/42901ff3c79bd4dcb77433f745c52d28/flightDeals/prices"
    response = requests.get(url=url)
    data = json.dumps(response.json(), indent=4)
    print(data)

add_iata_codes()
#get_details()