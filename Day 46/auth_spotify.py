import requests

class GetToken:
    # This clas is respnsible for generating bearer token
    def __init__(self):
        self.url = "https://accounts.spotify.com/api/token"
        self.body = {
            "grant_type": "client_credentials",
            "client_id": "70e27ae4bed648fe92d4f0befdfe0848",
            "client_secret": "23a99e150e934e87a3a69e0779695539"
        }
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.bearer_token = []


    def getToken(self):
        response = requests.post(self.url, params=self.body, headers=self.header)
        print("Status Code:", response.status_code)
        data = response.json()
        self.bearer_token = data["access_token"]
        print(self.bearer_token)

token = GetToken()
token.getToken()