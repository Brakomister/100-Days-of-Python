# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import requests
import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

flight_data = FlightData()
flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

SHEET_ENDPOINT = "https://api.sheety.co/6720116c401ba774d6bf0dfd0f893ec5/copyOfFlightDeals/prices"

response = requests.get(url=SHEET_ENDPOINT)
sheet_data = response.json()["prices"]

for flight in sheet_data:
    flight_code = flight["iataCode"]
    data = flight_search.cheaper_flight(flight_code)
    flight_details = flight_data.get_data(data)
    notification_manager.send_alert(flight_details, sheet_data)

