from selenium import webdriver
from selenium.webriver.common.by import By


# Keep Chrome browser open after program finishes
chrome_options = webdriverChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# will only give the first search result:
wp_number = driver.find_element_by_css_selector("#articlecount a")

print(wp_number.text)
