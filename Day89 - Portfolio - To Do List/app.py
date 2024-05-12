from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app=Flask(__name__)

# ------- Connect to Tasks DB -------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)  # Initialize db within the app context
app.config['SECRET_KEY'] = "secretsecret"
Bootstrap(app)

#----------------------------

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean,default=False)

@app.route('/')
def home():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks= tasks)



if __name__ == '__main__':
    app.run(debug=True)

