from flask import Flask, render_template
import random
from datetime import datetime as dt
import requests
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = dt.now().year
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<string:some_name>')
def guess(some_name):
    some_name = some_name.title()

    # --------------- Accessing gender.io ----------- #
    gender_response = requests.get(f'https://api.genderize.io?name={some_name}')
    gender_guess = gender_response.json()["gender"]

    age_response = requests.get(f'https://api.agify.io?name={some_name}')
    age_guess = age_response.json()['age']
    return render_template('guess.html', name=some_name, gender=gender_guess, age=age_guess)


if __name__ == "__main__":
    app.run(debug=True)
