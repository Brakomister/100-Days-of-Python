##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

letters = ["letter_1", "letter_2", "letter_3"]

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
birthday_dict = birthdays.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for item in birthday_dict:
    if now.day == item["day"] and now.month == item["month"]:
        name = item["name"]
        email = item["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person'sactual name from birthdays.csv
        letter_name = random.choice(letters)
        with open(f"letter_templates/{letter_name}.txt") as file:
            letter = file.read().replace("[NAME]", name)

# 4. Send the letter generated in step 3 to that person's email address.
        my_email = "kbrako.asante@gmail.com"
        password = "dgsagvrraeuebojp"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(to_addrs=email, from_addr=my_email, msg=f"Subject:Happy Birthday!\n\n{letter}")

