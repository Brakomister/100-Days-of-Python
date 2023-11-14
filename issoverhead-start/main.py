import requests
from datetime import datetime
import smtplib

MY_LAT = 5.603717  # Your latitude
MY_LONG = -0.186964  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
diff_latitude = iss_latitude - MY_LAT
diff_longitude = iss_longitude - MY_LONG

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
if -5 <= diff_longitude <= 5 and -5 <= diff_latitude <= 5 and time_now.hour > sunset:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    MY_EMAIL = "kbrako.asante@gmail.com"
    PASSWORD = "crglljryzhxwqsjm"
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(to_addrs="clarkkentclark876@gmail.com", from_addr=MY_EMAIL, msg="Look up")

# BONUS: run the code every 60 seconds.
