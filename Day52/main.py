# ------------CONSTANTS------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

# Set the path to your ChromeDriver executable
CHROME_DRIVER_PATH = CHROME_DRIVER_PATH

# Instagram account details for the targeted account
SIMILAR_ACCOUNT = "buzzfeedtasty"
USERNAME = INSTAGRAM_USERNAME
PASSWORD = INSTAGRAM_PASSWORD

# ------------INSTAGRAM FOLLOWER BOT------------

class InstaFollower:

    def __init__(self, path):
        # Initialize the webdriver with the specified ChromeDriver path
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        # Open the Instagram login page, enter credentials, and submit
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        # Navigate to the followers list of the specified Instagram account
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        # Click on the followers count to open the followers modal
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        # Scroll through the followers modal to load more followers
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        # Follow users listed in the followers modal
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                # Handle cases where a popup intercepts the click, such as a confirmation dialog
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


# Create an instance of the InstaFollower bot, login, find followers, and follow
bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
