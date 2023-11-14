import time


from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "< p>Hello, World!</p>"


@app.route("/<name>")
def greet(name):
    return f"Hello there {name}"


def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '<b>'
    return wrapper_function


@app.route("/bye")
@make_bold
def bye():
    return "Bye"


print(bye())


if __name__ == '__main__':
    app.run(debug=True)


# def delayed_function(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#
#     return wrapper_function
#
#
# def say_hello():
#     print("Hello")
#
#
# say_hello()
