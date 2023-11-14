from flask import Flask
import random

rand_num = random.randint(0, 9)
print(rand_num)

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o" \
           "7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route("/<int:number>")
def choose(number):
    if rand_num < number:
        return "<h1>Ha! Too high, partner.</h1>"

    elif rand_num > number:
        return "<h1>Sheesh! Too low, partner.</h1>"

    else:
        return "<h1>Spot on, partner!</h1>"


if __name__ == "__main__":
    app.run(debug=True)



