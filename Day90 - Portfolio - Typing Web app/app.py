from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secretsecret"
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['text'] = request.form['text']  # Save text to session
        session['last_timestamp'] = datetime.now().timestamp()  # Save last timestamp as a float

    text = session.get('text', '')
    last_timestamp = session.get('last_timestamp')

    # Clear text if more than 5 seconds have passed
    if last_timestamp:
        last_timestamp = datetime.fromtimestamp(last_timestamp)  # Convert float to datetime object
        time_passed = datetime.now() - last_timestamp
        if time_passed.total_seconds() > 5:
            session.pop('text', None)
            session.pop('last_timestamp', None)
            text = ''

    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
