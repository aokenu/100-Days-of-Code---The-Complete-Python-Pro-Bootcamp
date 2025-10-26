from bs4 import BeautifulSoup
import requests
from auth_spotify import GetToken



URL = "https://www.billboard.com/charts/hot-100/"


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Headers (must be comma-separated key-value pairs)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}


# Fetch the Billboard page for the given date
response = requests.get(f"{URL}{date}", headers=headers)
data = response.text
# print(data)


# Create a BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')

# print(soup)

# Extract song titles — Billboard uses a specific class for this
song_names_spans = soup.select("li.o-chart-results-list__item h3#title-of-a-story")

# Using list comprehension to itterate over the song_name_spans
hit_songs = [song.get_text(strip=True) for song in song_names_spans]

with open("hit_song.csv", "w", encoding="utf-8", newline="") as file:
    writer = file.writelines(songs + "\n" for songs in hit_songs)

print(hit_songs)


token = GetToken()

token.getToken()