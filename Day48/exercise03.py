from selenium import webdriver
from selenium.webriver.common.by import By
from selenium.webriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriverChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.get("https.secure-retreat-92358.herokuapp.com")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Negar")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Norouzi")

email = driver.find_element_by_name("email")
email.send_keys("python@gmail.com")

sign_up_button = driver.find_element_by_css_selector("form button")
sign_up_button.click()

driver.quite()
