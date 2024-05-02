from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from form import *
from random import choice

app = Flask(__name__)

# ------- Connect to DB -------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)  # Initialize db within the app context
app.config['SECRET_KEY'] = "secretsecret"
Bootstrap(app)


# ----- Cafe TABLE Configuration -----
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def convert_to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/all', methods=['GET', 'POST'])
def get_all_cafes():
    form = CafeSortForm()
    sort_by = request.form.get('sort_by', 'id')  # Default sorting by ID
    all_cafes = Cafe.query.order_by(sort_by).all()
    return render_template('all_cafe.html', all_cafes=[cafe.convert_to_dict() for cafe in all_cafes], form=form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    return render_template("signup.html", form=form)


@app.route('/random')
def random():
    form = CafeForm()
    all_cafes = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes)
    return render_template('random.html', cafes=[random_cafe], form=form)


@app.route("/search", methods=["GET", "POST"])
def search():
    form = Search()
    if form.validate_on_submit():
        location = form.location.data
        result = db.session.query(Cafe).filter(Cafe.location == location)
        return render_template('search.html', form=form, cafes=result)
    return render_template('search.html', form=form)


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            location=form.location.data,
            open=form.open.data,
            close=form.close.data,
            coffee_rating=form.coffee_rating.data,
            wifi_rating=form.wifi_rating.data,
            power_rating=form.power_rating.data
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('all_cafes'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
