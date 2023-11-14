# import smtplib
#
# my_email = "clarkkentclark876@gmail.com"
# password = "szriegcagannlpph"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="kwamebrako.asante@yahoo.com",
#         msg="Subject:Hello\n\nHow are you doing?")

import datetime as dt
import smtplib
import random

current_day = dt.datetime.now().weekday()

if current_day == 3:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    my_email = "clarkkentclark876@gmail.com"
    password = "szriegcagannlpph"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kwamebrako.asante@yahoo.com",
            msg=f"Subject:Hello\n\n{quote}")
