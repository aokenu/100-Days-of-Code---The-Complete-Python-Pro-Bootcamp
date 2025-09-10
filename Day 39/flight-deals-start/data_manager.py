import requests
import json



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = None
        self.url = "https://api.sheety.co/42901ff3c79bd4dcb77433f745c52d28/flightDeals/prices"

    def get_cities(self):
        self.response = requests.get(url=self.url)
        data = self.response.json()

        # Extract all city values
        cities = [item["city"] for item in data["prices"]]
        return cities




