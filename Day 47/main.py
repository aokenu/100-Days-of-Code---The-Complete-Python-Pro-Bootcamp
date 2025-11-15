import requests
import json
from bs4 import BeautifulSoup
from item_price import PriceTag


# creating an instance of PriceTag
item_price = PriceTag()

# calling the get_price method from the PriceTag class
item_price.get_price()


