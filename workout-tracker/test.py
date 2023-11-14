import requests
from datetime import datetime

# GENDER = YOUR GENDER
# WEIGHT_KG = YOUR WEIGHT
# HEIGHT_CM = YOUR HEIGHT
# AGE = YOUR AGE

APP_ID = "6396c65e"
API_KEY = "7ec41960c41689e82c33e5ebfcf8866e"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/6720116c401ba774d6bf0dfd0f893ec5/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 100,
    "height_cm": 150,
    "age": 18
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)