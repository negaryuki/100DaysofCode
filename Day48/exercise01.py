from selenium import webdriver
from selenium.webriver.common.by import By


# Keep Chrome browser open after program finishes
chrome_options = webdriverChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https.python.org')


event_times = driver.find_elements_by_css_selector(".event-widget time")

event_names = driver.find_element_by_css_selector(".event-widget li a")

events = {}

for n in range(len(event_times)):
  events[n] :{
    "time": event_times[n].text,
    "name" event_names[n].text,    
  }

  
driver.quite() 
