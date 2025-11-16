import requests
from bs4 import BeautifulSoup


# define a class 
class PriceTag:
    
    def __init__(self):

        self.URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1&language=en_US&currency=USD"
        self.header = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
                "Accept-Language": "en-US,en;q=0.9,it;q=0.8,de;q=0.7",  
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36", 
            }        

        # calling the url with a get request
        self.response = requests.get(url=self.URL, headers=self.header)
        self.data = self.response.text


    def get_price(self):
        # create an instance of beatifulsoup
        self.soup = BeautifulSoup(self.data, 'html.parser')

        # extracting the content of the web page using the created instance of Beautifulsoup
        web_page = self.soup.find(name="span", class_="aok-offscreen")
        web_text = web_page.text
        get_price = float(web_text.split(" ")[1][1:])


        # return the output of the scrapped value
        return get_price
   


# price = PriceTag()
# check_price = price.get_price()
# print(check_price)