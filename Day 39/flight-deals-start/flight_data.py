import json
from datetime import datetime, timedelta
import requests
from flight_search import FlightSearch


class FlightData:
    """This class is responsible for structuring and retrieving flight data."""

    def __init__(self, flight_search: FlightSearch):
        self.flight_search = flight_search
        self.url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.header = {
            "Authorization": f"Bearer {self.flight_search.get_token()}"
        }

    def get_flight_offers(self, origin: str, destination: str):
        """Get flight offers between origin and destination within 6 months."""
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        six_months = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": tomorrow,
            "returnDate": six_months,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": 10
        }

        response = requests.get(url=self.url, headers=self.header, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return None

        data = response.json()
        print(json.dumps(data, indent=4))
        return data


    def find_cheapest_flight(self, data):
        """Extract the cheapest flight price from the API JSON."""
        if not data or "data" not in data or len(data["data"]) == 0:
            return "N/A"

        try:
            # Sort all offers by total price
            offers = data["data"]
            cheapest = min(
                offers,
                key=lambda x: float(x["price"]["total"])
            )
            price = cheapest["price"]["total"]
            return f"£{price}"
        except (KeyError, ValueError, TypeError):
            return "N/A"

    # To get the list of IATA codes from the Google sheet
    def get_iata_details(self):
        url = "https://api.sheety.co/42901ff3c79bd4dcb77433f745c52d28/flightDeals/prices"
        response = requests.get(url=url)
        response.raise_for_status()

        data = response.json()

        # extract the list of city rows
        prices_list = data["prices"]

        # Extract all IATA codes from the list
        iata_codes = [item["iataCode"] for item in prices_list]

        print("IATA Codes:", iata_codes)
        return iata_codes



if __name__ == "__main__":
    flight_search = FlightSearch()
    flight_data = FlightData(flight_search)


    for city_code in flight_data.get_iata_details(): # iterating through the list of IATA codes from the Google sheet
        data = flight_data.get_flight_offers("LON", city_code)
        price = flight_data.find_cheapest_flight(data)
        print(f"{city_code}: {price}")