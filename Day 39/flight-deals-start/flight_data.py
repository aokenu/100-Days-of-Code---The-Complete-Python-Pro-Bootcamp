import json

import requests
from flight_search import FlightSearch


class FlightData:
    """This class is responsible for structuring and retrieving flight data."""

    def __init__(self, flight_search: FlightSearch):
        self.flight_search = flight_search
        self.url = "https://test.api.amadeus.com//v2/shopping/flight-offers"
        self.header = {
            "Authorization": f"Bearer {self.flight_search.get_token()}"
        }

    def flight_offers(self):
        params = {
            "originLocationCode": "LON",
            "destinationLocationCode": "PAR",
            "departureDate": "2025-10-05",
            "adults": 1,
            "nonStop": "false",
            "max": 5
        }

        response = requests.get(url=self.url, headers=self.header, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return None

        data = response.json()
        print(json.dumps(data, indent=4))
        return data



flight_search = FlightSearch()
offers = FlightData(flight_search)
flights = offers.flight_offers()

print(flights)