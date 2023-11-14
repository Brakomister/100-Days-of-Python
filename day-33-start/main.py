import requests
import datetime as dt

# ------ MY POSITIONS ------ #
MY_LAT = 5.603717
MY_LONG = -0.186964

# ------ ISS POSITIONS ------ #
response = requests.get("https://api.sunrise-sunset.org/json.")


