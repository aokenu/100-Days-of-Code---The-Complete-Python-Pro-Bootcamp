import requests

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
    "id": "graph1",
    "name": "Fitness Walk",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

get_user = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(get_user.text)