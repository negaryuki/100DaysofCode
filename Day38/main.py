import requests
from datetime import datetime  

#--------------- USER PROFILE ----------------
GENDER = "female"
WEIGHT_KG = 70
HEIGHT_CM = 166
AGE = 28
#--------------- API INFO  -------------------

APP_ID = "APP_ID"
API_KEY = "API_KEY"

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/62bf219154ff52ae3cb0172f15a57ff7/myWorkout/workouts"

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

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
  input_sheet = {
    "workout":{
      "date": today_date,
      "time": now_time,
      "exercise": exercise["name"].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"]
  }
}

sheet_response = requests.post(sheet_endpoint, json = input_sheet)

print(sheet_response.text)


