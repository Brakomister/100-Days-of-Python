from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/kbrak/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# ---- Navigating to Login Page ------ #
driver.get("https://tinder.com/")
sleep(2)

login = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div['
                                     '2]/div[2]/a/div[2]/div[2]')
login.click()
sleep(2)

fb_button = driver.find_element("xpath", '/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div['
                                         '2]/button/div[2]/div[2]/div/div')
fb_button.click()

# ---- Login with Facebook ---- #
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
sleep(2)

email_box = driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_box.send_keys('0242218648')
pass_box = driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
pass_box.send_keys('0246599231')
login = driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
login.click()
sleep(2)

# while True:
#     pass

continue_ = driver.find_element('xpath', '/html/body/div/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/div['
                                         '1]/div/div/div/div[1]')
continue_.click()
sleep(2)

# driver.switch_to.window(base_window)
# print(driver.title)

