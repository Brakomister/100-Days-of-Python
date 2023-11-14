import requests
from datetime import datetime
import os

os.environ["APP_ID"] = "6396c65e"
os.environ["API_KEY"] = "7ec41960c41689e82c33e5ebfcf8866e"
os.environ["SHEET_ENDPOINT"] = "https://api.sheety.co/6720116c401ba774d6bf0dfd0f893ec5/workoutTracking/workouts"
os.environ["TOKEN"] = "iamaboy"

exercise = input("Tell me what exercise you've tried today:")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_params = {
    "query": exercise
}
exercise_headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY")
}
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercises = response.json()["exercises"]

name_list = [item['name'] for item in exercises]
duration_list = [item['duration_min'] for item in exercises]
calories_list = [item['nf_calories'] for item in exercises]

for i in range(0, len(name_list)):
    body = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": name_list[i].title(),
            "duration": duration_list[i],
            "calories": calories_list[i]
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {os.environ.get('TOKEN')}"
    }
    sheets_response = requests.post(os.environ.get("SHEET_ENDPOINT"), json=body, headers=bearer_headers)
    print(sheets_response.text)

