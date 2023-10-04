import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_APIKEY = "****"
NEWS_APIKEY = "****"
TWILIO_SID ="****"
TWILIO_AUTH_TOKEN = "****"

#----------------- PARAMETERS -----------------------

alpha_vantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_APIKEY,
}

news_api_parameters = {
    "apiKey": NEWS_APIKEY,
    "qInTitle": COMPANY_NAME,
}

#----------------- REQUESTS  -----------------------
alpha_vantage_response = requests.get(STOCK_ENDPOINT, params=alpha_vantage_parameters)
alpha_vantage_response.raise_for_status()
stock_data = alpha_vantage_response.json()


news_api_response = requests.get(NEWS_ENDPOINT, params=news_api_parameters)
news_api_response.raise_for_status()
news_data = news_api_response.json()

#-------------------------------------------------

data_list = [value for (key,value) in stock_data.items()]


yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4.close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4.close"]

# abs = absolute number (without negatives)

difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price)0
up_down= None

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

difference_percent = round((difference / float(yesterday_closing_price)) * 100)


#-------------------------------------------------

articles = news_data["articles"]
three_articles = articles[:3]

formatted_articles =[f"{STOCK_NAME}: {up_down}{difference_percent}%\nHeadlines:{article['title']}. \nBrief:{article['description']} for artice in three_articlels"]

#-------------------------------------------------

if abs(difference_percent) > 5:

  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
  for article in formatted_articles:
    message = client.messages.create(
      body = article,
      from= "1234"
      to="1234"      
      )




