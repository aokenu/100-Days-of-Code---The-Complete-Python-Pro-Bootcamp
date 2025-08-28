import requests
import json
from twilio.rest import Client
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_MKT_URL = "https://www.alphavantage.co/query"
stock_market_apikey = os.environ.get("STOCK_MKT_API")

stk_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stock_market_apikey
}

tesla_stock = requests.get(STOCK_MKT_URL, stk_parameters)
tesla_stock.raise_for_status()

# Convert to json
tesla_stock_json = tesla_stock.json()

# Access the "Time Series (60min)" data
time_series = tesla_stock_json
print(time_series)



# first_timestamp = list(time_series.keys())[0]
# tesla_stock_data = time_series[first_timestamp]
# # Get the first timestamp
#
# print(json.dumps(tesla_stock_data, indent=4))


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

TESLA_NEWS_URL = "https://newsapi.org/v2/everything"
news_api_key = os.environ.get("NEWS_API_KEY")

tesla_parameters = {
    "q": "tesla",
    "from": "yesterday",
    "sortBy": "published",
    "apikey": news_api_key
}

get_news = requests.get(TESLA_NEWS_URL, tesla_parameters)
get_news.raise_for_status()
news_data = get_news.json()["articles"][0:3]
# print(json.dumps(news_data, indent=4))


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

