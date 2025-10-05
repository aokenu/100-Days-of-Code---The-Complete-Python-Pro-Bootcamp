import requests
import json


id_range = range(2, 11, 1)
ObjectID = []



iata_Code = ["PAR", "FRA", "TOK", "HON", "ISB", "KLP", "NYC", "SAN", "DUB"]




def insert_details():
    for id in id_range:
        ObjectID = id

        # print(ObjectID)
        code = (iata_Code[id -2])

        body = {
            "price": {
                "iataCode": code
            }
        }

        url = f"https://api.sheety.co/42901ff3c79bd4dcb77433f745c52d28/flightDeals/prices/{ObjectID}"
        response = requests.put(url=url, json=body)
        print(f"Updating row {ObjectID} with code {code} .....")
        print(response.text)


def get_details():
    url = "https://api.sheety.co/42901ff3c79bd4dcb77433f745c52d28/flightDeals/prices"
    response = requests.get(url=url)
    data = json.dumps(response.json(), indent=4)
    print(data)

# Get the list of IATA Codes from the Google sheet
def get_iata_details():
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


get_iata_details()

