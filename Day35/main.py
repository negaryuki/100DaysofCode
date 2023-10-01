import requests


OWM_endpoint  = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "c80067c09286776bc601fa3c8cdf80c5"

weather_params = {
  "lat": 51.507351,
  "lon": -0.127758,
  "appid": api_key,
}

response = requests.get(OWM_endpoint, params= weather_params)

print(response.status_code)
