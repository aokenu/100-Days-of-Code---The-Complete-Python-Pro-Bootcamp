import requests
import json
from bs4 import BeautifulSoup


# define a class 
class PriceTag:
    
    def __init__(self):

        self.URL = "https://appbrewery.github.io/instant_pot/"

        # calling the url with a get request
        self.response = requests.get(self.URL)
        self.data = self.response.text

    def get_price(self):
        # create an instance of beatifulsoup
        self.soup = BeautifulSoup(self.data, 'html.parser')

        # extracting the content of the web page using the created instance of Beautifulsoup
        web_page = self.soup.find(name="span", class_="a-price-whole")
        get_price = float(web_page.text)

        # Print the output of the scrapped value
        print(get_price)