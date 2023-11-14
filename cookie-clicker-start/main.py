from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:/Users/kbrak/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


# ---- Function to check the most expensive purchase available
def make_purchase():
    print(amounts)
    global my_money
    for i in range(len(purchases)):
        if amounts[i] <= int(my_money):
            print(f"The store purchase available is : {driver.find_element('id', _ids[i]).text}")
            driver.find_element("id", _ids[i]).click()


def find_amount(purchase):
    for content in purchase.text.split(" "):
        if "\n" in content:
            amount = content.split("\n")[0].replace(",", "")
            return int(amount)


# ---- Finding needed elements from the cookie game website ----- #
cookie = driver.find_element('id', 'cookie')
my_money = driver.find_element('id', 'money').text

_ids = ['buyTime machine', 'buyPortal', 'buyAlchemy lab', 'buyShipment', 'buyMine', 'buyFactory',
        'buyGrandma', 'buyCursor']

is_on = True
five_min = time.time() + 300
timeout = time.time() + 5

# ----- Playing the game ----- #
while is_on:
    cookie.click()

    if time.time() >= timeout:

        purchases = [driver.find_element('id', _id) for _id in _ids]
        amounts = [find_amount(purchase) for purchase in purchases]

        for i in range(len(purchases)):
            if amounts[i] <= int(my_money):

                time.sleep(1)
                purchase = driver.find_element('id', _ids[i])
                purchase.click()

        timeout = time.time() + 5
    my_money = driver.find_element('id', 'money').text
    if time.time() >= five_min:
        break
