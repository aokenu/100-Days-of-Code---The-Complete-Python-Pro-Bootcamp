import requests
import base64
import urllib.parse

class GetToken:
    # This clas is respnsible for generating bearer token
    def __init__(self):
        self.SPOTIFY_CLIENT_ID = "70e27ae4bed648fe92d4f0befdfe0848"
        self.SPOTIFY_CLIENT_SECRET = "883f4f76eef64cc78731843f4c71be45"
        self.redirect_uri = "http://127.0.0.1:80/callback.php"
        self.url = "https://accounts.spotify.com/api/token"
        self.body = {
            "grant_type": "client_credentials",
            "client_id": self.SPOTIFY_CLIENT_ID,
            "client_secret": self.SPOTIFY_CLIENT_SECRET
        }
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        self.OAuth = None


    def get_authorize_url(self):
        params = {
            "client_id": self.SPOTIFY_CLIENT_ID,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": "playlist-modify-private playlist-modify-public",
            "state": "xyz123"
        }

        query = urllib.parse.urlencode(params)
        url = f"https://accounts.spotify.com/authorize?{query}"
        return url


    def get_OAuth(self, code):
            auth_str = f"{self.SPOTIFY_CLIENT_ID}:{self.SPOTIFY_CLIENT_SECRET}"
            b64_auth = base64.b64encode(auth_str.encode()).decode()

            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {b64_auth}"
            }

            body = {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": self.redirect_uri
            }

            response = requests.post(self.url, data=body, headers=headers)
            self.OAuth = response.json()
            return self.OAuth




