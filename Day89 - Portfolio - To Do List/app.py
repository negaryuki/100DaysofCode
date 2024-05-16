from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import *

app = Flask(__name__)

# ------- Connect to Tasks DB -------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = "secretsecret"
db = SQLAlchemy(app)
Bootstrap(app)


# Define the Tasks model
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)


# Create database tables
# with app.app_context():
#    db.create_all()


@app.route('/')
def home():
    form = TaskForm()
    if request.method == 'POST' and form.validate_on_submit():
        date = form.date.data
        if date:
            tasks = Tasks.query.filter_by(date=date).all()
            return render_template('base.html', form=form, tasks=tasks)

        else:
            error_msg = "Please enter a date first"
            return render_template(url_for('home'), error_msg=error_msg)

    return render_template('base.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Tasks(date=form.date.data, description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
