from selenium import webdriver
from selenium.webriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriverChromeOptions()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/STANLEY-Quencher-FlowState-Tumbler-Orchid/dp/B0C3GL93H8/ref=sr_1_5?crid=28VFL8NPF20TE&keywords=Stanley+quencher+H2.0+flowstate+tumbler&qid=1699436880&sprefix=stanley+quencher+h2.0+flowstate+tumbl%2Caps%2C403&sr=8-5")


price_dollar =driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")

print(f'Price is:{price_dollar.text}.{price_cents.text}')


driver2 = webdriver.Chrome(options=chrome_options)
driver2.get('https.python.org')

search_bar = driver2.find_element(By.NAME, value=q)
print(search_bar.get_attribute("placeholder"))

button = driver2.find_element(By.ID, value="submit")
print(button.size)


documentation_link = driver2.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

# locating a specific elememy by path --> xpath:
  
bug_link = driver2.find_element(By.XPATH, value ='//*[@id="site-map"]/div[2]/div/ul/li[3/a')
print(bug_link.text)

# driver.close() ---> closes Chrome immidiatly after the page loads
driver.quite() #---> will close the entier Browser 
