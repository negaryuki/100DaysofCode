import requests
from twilio.rest import client

OWM_endpoint  = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "024ac76d4f00bf1ef45f21ae9d7b3c84"


weather_params = {
  "lat": 51.507351,
  "lon": -0.127758,
  "appid": api_key,
  "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params= weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
  condition_code = (hour_data["weather"][0]["id"])
  if int(condition_code) < 700:
    will_rain = True

if will_rain:
  client = client.messages \
  .create(
    body = "🌧 bring an umbrella",
    from = "12345667",
    to = "1234567"
    )
  

