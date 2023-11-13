from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<h1 style = "text-align:center">Hello, World!</h1>' \
    '<p>This is a Paragraph</p>' \
    '<img src="https://media.giphy.com/media/c76IJLufpNwSULPk77/giphy.gif" width=200>'

 
@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name} ! you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
