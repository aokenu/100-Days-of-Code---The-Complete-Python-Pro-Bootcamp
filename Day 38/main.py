import requests
import json
from datetime import datetime
import os



API_ID = os.environ["API_ID"]
API_KEY = os.environ["API_KEY"]

URL = "https://trackapi.nutritionix.com"

QUERY = input("Tell me what you did today:")

parameters = {
    "query": f"{QUERY}"
}

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

ENDPOINT = f"{URL}/v2/natural/exercise"

response = requests.post(ENDPOINT, parameters, headers=headers)
data = response.json()
# print(json.dumps(data, indent=4))

exercise = data["exercises"][0]["name"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

date = datetime.now().strftime("%d/%m/%Y")

datetime.now()
time = datetime.now().strftime("%X")

url = os.environ["SHEETY_URL"]
body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

TOKEN = os.environ["SHEETY_TOKEN"]

header = {
    "Authorization": f"Bearer {TOKEN}"
}

update_workout = requests.post(url=url, json=body, headers=header)
print(update_workout.text)
