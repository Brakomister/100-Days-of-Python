from flight_search import FlightSearch


class FlightData:

    def get_data(self, data):

        data_dict = {
            "price": data["price"],
            "DCN": data["cityFrom"],
            "DAIC": data['flyFrom'],
            "ACN": data['cityTo'],
            "AAIC": data['flyTo'],
            "outbound": data['utc_arrival'][:10],
            "inbound": data['utc_departure'][:10],
        }
        print(data_dict)
        return data_dict
