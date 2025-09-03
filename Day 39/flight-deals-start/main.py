from data_manager import DataManager
from flight_search import FlightSearch

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.




# Create an object instance of DataManager
data_prices = DataManager()
#
sheet_data = data_prices.get_prices()
# print(sheet_data)


# Create an object instance of FlightSearch
flight_data = FlightSearch()
# flight_data.get_flight_offers()

print(flight_data.get_token())
print(flight_data.get_flight_offers())

fs = FlightSearch()
fs.get_token()
iata_codes = fs.get_flight_offers(keyword="Paris")
print(iata_codes)