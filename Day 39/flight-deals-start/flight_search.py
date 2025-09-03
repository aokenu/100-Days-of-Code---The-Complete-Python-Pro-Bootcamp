import requests
from data_manager import DataManager
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, data_manager=None):
        self.DataManager = data_manager
        self.flight_header = None
        self.token = None
        self.api_key = os.environ["FLIGHT_API_KEY"]
        self.api_secret = os.environ["FLIGHT_API_SECRET"]
        self.url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        # self.endpoint = "/shopping/flight-offers"
        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.token_param = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }



    def get_token(self):
        token_response = requests.post(url=self.token_endpoint, data=self.token_param, headers=self.header)
        self.token = token_response.json()["access_token"]
        return self.token

    def get_flight_offers(self, keyword=""):
        self.flight_header = {
            "Authorization": f"Bearer {self.token}"
        }

        self.parameter = {
            "keyword": keyword,
            "max": "10"
        }
        response = requests.get(url=self.url, params=self.parameter, headers=self.flight_header)
        flight_offers = response.json()

        # Extract all IATA codes safely
        iata_codes = [item.get("iataCode") for item in flight_offers.get("data", [])]
        return iata_codes
