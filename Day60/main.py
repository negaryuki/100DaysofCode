from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def receive_data():
    return "Success! Form submitted!!"



if __name__ == "__main__":
    app.run(debug=True, port=5001)
