from bs4 import BeautifulSoup
import requests


PRODUCT_URL = "https://www.amazon.com/Japanese-Samurai-Hannya-Demon-Monster/dp/B09Z1QDF15/ref=sr_1_1?crid" \
              "=2TUTYSN65LZJ0&keywords=oni%2Bmask%2Bjapanese&qid=1682195823&sprefix=oni%2Bmask%2Caps%2C984&sr=8-1&th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=PRODUCT_URL, headers=HEADERS)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

# Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.
price = soup.find(class_="a-button")
print(price)
