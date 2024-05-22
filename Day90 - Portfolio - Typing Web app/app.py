from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "secretsecret"
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        session['text'] = text  # save text to session
        session['last_timestamp'] = datetime.now()  # save last timestamp to session
        return redirect(url_for('home'))

    if 'last_timestamp' in session:
        now = datetime.now()
        time_passed = (now - session['last_timestamp']).total_seconds()
        if time_passed > 5:
            session.pop('text', None)   # dict.pop(key, default) None prevents a KeyError

    text = session.get('text', '')
    return render_template('index.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
