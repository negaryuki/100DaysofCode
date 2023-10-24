import requests

#--------------- USER PROFILE ----------------

GENDER = "female"
WEIGHT_KG = 70
HEIGHT_CM = 166
AGE = 28
#--------------- API INFO  -------------------

APP_ID = "APP_ID"
API_KEY = "API_KEY"

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
excercise_text = input("What Exercise did you do?")

headers = {
  
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,  
}


parameters = {
  "query": excercise_text,
  "gender": GENDER,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE 
}

response = requests.post(excercise_endpoint, json= parameters, headers = headers)

result = response.json()

print(result)
