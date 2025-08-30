import requests
from datetime import datetime

USERNAME = "goldstine86"
TOKEN = "be6db712e18kw8dshd"

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create_response = requests.post(url=pixela_endpoint, json=parameters)
# print(create_response.text)

# Create a Graph for the user
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Defining the parameters for the graph
graph_config = {
    "id": "graph2",
    "name": "Learning Python",
    "unit": "Commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# get_user = requests.get(url=graph_endpoint, json=graph_config, headers=headers)
# print(get_user.text)


# Posting a pixel
GRAPH2 =  "graph2"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH2}"

today = datetime.now()

# Defining the config
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

# Creating the authorization header
pixel_headers = {
    "X-USER-TOKEN": TOKEN
}

# Calling the POST request to add a pixel for each python topic I studied
create_pixel = requests.post(url=pixel_endpoint, json=pixel_config, headers=pixel_headers)
print(create_pixel.text)