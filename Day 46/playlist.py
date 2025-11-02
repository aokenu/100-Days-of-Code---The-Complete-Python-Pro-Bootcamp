import requests
from auth_spotify import GetToken


class PlayList(GetToken):

    def __init__(self, bearer_token):
        super().__init__()  # 🔥 Inherit token logic from GetToken
        self.user_id = "31v2xt4iowhthmx3wb56fjq4s344"
        self.spotify_search_url = "https://api.spotify.com/v1"
        self.search_song = "https://api.spotify.com/v1/search?q=remaster%20track%3ABack%20In%20The%20Saddle&type=track"
        self.create_playlist = f"/users/{self.user_id}/playlists"
        self.track_id = 0
        self.track_name = 0

        # Get bearer token
        self.bearer_token = bearer_token
        self.header = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }


    def get_userId(self):
        response = requests.get(self.spotify_search_url + "/me", headers=self.header)
        data = response.json()
        print(data)


    def createPlaylist(self):
        self.body = {
            "name": "New Playlist",
            "description": "New playlist description",
            "public": False
        }
        response = requests.post(self.spotify_search_url + self.create_playlist, json=self.body, headers=self.header)
        status = response.status_code
        data = response.text
        print(data)


    def search_track(self):
        self.params = {
            "q": "remaster track:Back In The Saddle",
            "type": "track"
            }
            
        response = requests.get(self.search_song, headers=self.header)
        data = response.json()
        self.track_id = data["tracks"]["items"][0]["id"]
        self.track_name = data["tracks"]["items"][0]["name"]
        return self.track_id
        return self.track_name
    
    def add_track(self):
        self.data = {
        "uris": [
            self.track_id
        ],
        "position": 0
        }
        response = requests.post(self.spotify_search_url + f"/playlists/{self.track_id}/tracks", params=self.data, headers=self.header)
        data = response.json()
        print(response.text)
        if data.status_code == 200:
            print(f"track name {self.track_name} successfully added to playlist")


