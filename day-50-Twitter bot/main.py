from selenium import webdriver
from time import sleep

PROMISED_DOWN = 49
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/Users/kbrak/Development/chromedriver"
TWITTER_EMAIL = 'omegaishere126@gmail.com'
TWITTER_PASSWORD = 'independentAgya@04'


# --------- Create a class ------------ #
class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)

        start = self.driver.find_element('class name', 'start-text')
        start.click()
        sleep(60)

        down_data = self.driver.find_element('class name', 'download-speed')
        up_data = self.driver.find_element('class name', 'upload-speed')
        data = (down_data.text, up_data.text)
        return data

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login?redirect_after_login=%2F')
        sleep(2)

        self.driver.find_element('tag name', 'input').send_keys(TWITTER_EMAIL)
        self.driver.find_element('xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div['
                                          '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
        sleep(10)

        self.driver.find_element('xpath', '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div['
                                          '1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/'
                                          'input').send_keys(TWITTER_PASSWORD)
        self.driver.find_element('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                          '2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span/font/font').click()

        while True:
            pass



bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()
