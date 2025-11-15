import requests
import json
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/instant_pot/"

# calling the url with a get request
response = requests.get(URL)
data = response.text


# create an instance of beatifulsoup
soup = BeautifulSoup(data, 'html.parser')
web_page = soup.find(name="span", class_="a-price-whole")
get_price = float(web_page.text)
print(get_price)
