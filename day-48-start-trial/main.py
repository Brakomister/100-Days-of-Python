from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# The above import is used for automated typing of
chrome_driver_path = "C:/Users/kbrak/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element("class name", "green")
# print(price.text)

# search_bar = driver.find_element("name", element)

# logo = driver.find_element("css selector", "")

# driver.find_element("xpath", "//*[@id="site-map"]/div[2]/div/ul/li[3]/a")

# all_portals.click()
# search = driver.find_element("name", "search")
# search.send_keys()
# ----------- CHALLENGE: ------------ #
year_list = driver.find_elements("css selector", ".last li time")
event_list = driver.find_elements("css selector", ".event-widget li a")
my_dict = {}
for i in range(len(year_list)):
    # print(f"{year_list[i].text}: {event_list[i].text}")
    my_dict[i] = {"time": year_list[i].text, "name": event_list[i].text}

print(my_dict)
