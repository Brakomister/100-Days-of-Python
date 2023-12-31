from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/kbrak/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

n = driver.find_element("xpath", '//*[@id="articlecount"]/a[1]')
search = driver.find_element("name", "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()
