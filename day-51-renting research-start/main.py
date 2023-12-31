import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pprint

# --------- GET INFORMATION FROM RENTALS WEBSITE -------- #

url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C' \
      '%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122' \
      '.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22' \
      '%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D' \
      '%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22' \
      '%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B' \
      '%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price' \
      '%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom' \
      '%22%3A12%7D'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

addresses = [address.text for address in soup.find_all('address')]
prices = [price.text.split("+")[0] for price in soup.select('.jLQjry')]
links = [link['href'] for link in soup.select('.property-card-link')]


# ------------ FILLING GOOGLE FORMS ------------- #
class Driver:
    def __init__(self):
        chrome_driver_path = "C:/Users/kbrak/Development/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def fill_form(self, index):
        self.driver.get('https://forms.gle/ZiXbE4LnngJDByjp9')
        sleep(3)

        address = self.driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                    '2]/div/div[1]/div/div[1]/input')
        address.send_keys(addresses[index])
        price = self.driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                  '2]/div/div[1]/div/div[1]/input')
        price.send_keys(prices[index])
        link = self.driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
                                                 '2]/div/div[1]/div/div[1]/input')
        link.send_keys(links[index])

        self.driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()


bot = Driver()
for i in range(len(prices)):
    bot.fill_form(i)
while True:
    pass