from flask import Flask, render_template, request, redirect, url_for, flash
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
def add_cafe(new_cafe=None):
    form = CafeForm()
    if form.validate_on_submit():
        existing_cafe = Cafe.query.filter_by(name=form.name.data).first()
        if existing_cafe:
            return render_template('add.html', form=form, error="Cafe with this name already exists!")
        else:
            new_cafe = Cafe(
                name=form.name.data,
                map_url=form.map_url.data,
                img_url=form.img_url.data,
                location=form.location.data,
                has_sockets=form.has_sockets.data,
                has_toilet=form.has_toilet.data,
                has_wifi=form.has_wifi.data,
                can_take_calls=form.can_take_calls.data,
                seats=form.seats.data,
                coffee_price=form.seats.data)

            db.session.add(new_cafe)
            db.session.commit()
            return redirect(url_for('get_all_cafes'))
    return render_template('add.html', form=form)


@app.route('/update/<int:cafe_id>', methods=['GET', 'POST'])
def update(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if not cafe:
        flash('Cafe not found.', 'error')
        return redirect(url_for('home'))

    form = CafeForm(obj=cafe)
    if form.validate_on_submit():
        cafe.name = form.name.data
        cafe.location = form.location.data
        cafe.map_url = form.map_url.data
        cafe.img_url = form.img_url.data
        cafe.has_sockets = form.has_sockets.data
        cafe.has_toilet = form.has_toilet.data
        cafe.has_wifi = form.has_wifi.data
        cafe.can_take_calls = form.can_take_calls.data
        cafe.seats = form.seats.data
        cafe.coffee_price = form.coffee_price.data
        db.session.commit()  # Commit the changes to the database
        flash('Cafe information updated successfully.', 'success')
        return redirect(url_for('get_all_cafes'))

    return render_template('update.html', form=form, cafe=cafe)

if __name__ == '__main__':
    app.run(debug=True)
