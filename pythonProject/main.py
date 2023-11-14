import requests
api_key = "61ee858ab143a5e4bbeb52bd45237435"
OMW_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 5.759358,
    "lon": -0.225036,
    "appid": api_key,
}

response = requests.get(OMW_endpoint, params=weather_params)
print(response.json())
