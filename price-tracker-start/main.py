import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

product_url = "https://camelcamelcamel.com/product/B0B4N3WK4P"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url=product_url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
price = soup.select_one(".green").getText()
print(price)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
