import requests
import datetime as dt
from dateutil.relativedelta import relativedelta

SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
CHEAP_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
SEARCH_API_KEY = "YdWu0QX8sJomJE2FnCgK7S_VryQOeztZ"
HEADERS = {
    "apiKey": "YdWu0QX8sJomJE2FnCgK7S_VryQOeztZ"
}

class FlightSearch:

    def get_iata(self, city):
        parameters = {
            "term": city
        }
        response = requests.get(url=SEARCH_ENDPOINT, params=parameters, headers=HEADERS)
        return response.json()['locations'][0]['code']

    def cheaper_flight(self, code):
        date_from = dt.datetime.now()
        date_to = dt.datetime.now() + dt.timedelta(days=6*30)

        parameters = {
            "fly_from": "LON",
            "fly_to": code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP"
        }

        response = requests.get(url=CHEAP_ENDPOINT, params=parameters, headers=HEADERS)
        return response.json()["data"][0]
