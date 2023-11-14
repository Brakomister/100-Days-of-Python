import requests

SHEET_ENDPOINT = "https://api.sheety.co/6720116c401ba774d6bf0dfd0f893ec5/copyOfFlightDeals/prices"


class DataManager:

    def add_code(self, flight_data):
        row_endpoint = f"https://api.sheety.co/6720116c401ba774d6bf0dfd0f893ec5/copyOfFlightDeals" \
                       f"/prices/{flight_data['id']}"
        data = {
            "price": {
                "iataCode": flight_data["iataCode"]
            }
        }

        response = requests.put(url=row_endpoint, json=data)
        return response.json()[0]
