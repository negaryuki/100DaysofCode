# Importing necessary modules from Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# ----------CONSTANTS-------------------------
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "YOUR_CHROME_DRIVER_PATH"
TWITTER_EMAIL = "YOUR_TWITTER_EMAIL"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"

# Class definition for the InternetSpeedTwitterBot
class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        # Initializing the bot with the Chrome driver
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Opening the Speedtest website and initiating the speed test
        self.driver.get("https://www.speedtest.net/")
        # Uncomment the following lines to handle any pop-up banners
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()
        # time.sleep(3)

        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        # Extracting the upload and download speeds
        self.up = self.driver.find_element_by_xpath('''
            //*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span
        ''').text
        self.down = self.driver.find_element_by_xpath('''
            //*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span
        ''').text

    def tweet_at_provider(self):
        # Logging into Twitter and composing a tweet to the internet provider
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        # ———LOG IN ——
        email = self.driver.find_element_by_xpath('''
            //*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input
        ''')
        password = self.driver.find_element_by_xpath('''
            //*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input
        ''')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # Composing the tweet and sending it
        tweet_compose = self.driver.find_element_by_xpath('''
            //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div
        ''')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath('''
            //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]
        ''')
        tweet_button.click()
        time.sleep(2)
        # Quitting the browser session
        self.driver.quit()

# Creating an instance of the InternetSpeedTwitterBot and executing the actions
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
