import requests


STOCK_NAME = "TSLA"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_APIKEY = "****"
NEWS_APIKEY = "****"

#----------------- PARAMETERS -----------------------

alpha_vantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_VANTAGE_APIKEY,
}

news_api_parameters = {
    "q": f"{STOCK_NAME} Market Update",
    "pageSize": 3,
    "apiKey": NEWS_APIKEY,
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

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)0

difference_percent = (difference / float(yesterday_closing_price)) * 100

if difference_percent > 5:
  print("Get News")
