
import smtplib

email = "kbrako.asante@gmail.com"
password = "dgsagvrraeuebojp"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)