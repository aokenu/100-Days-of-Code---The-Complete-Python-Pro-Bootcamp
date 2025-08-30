import requests
import json



API_ID = "6bfe0f71"
API_KEY = "5a05160438dbf870ca4aebd049bbb874"

URL = "https://trackapi.nutritionix.com"

QUERY = "I ate 2 teaspoons of milk today"

parameters = {
    "query": f"{QUERY}"
}

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

ENDPOINT = f"{URL}/v2/natural/nutrients"

response = requests.post(ENDPOINT, parameters, headers=headers)
data = response.json()
print(json.dumps(data, indent=4))