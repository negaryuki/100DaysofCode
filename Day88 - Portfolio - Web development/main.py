from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from form import *

app = Flask(__name__)

# ------- Connect to DB -------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)  # Initialize db within the app context
app.config['SECRET_KEY'] = "secretsecret"


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


@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template("signup.html", form=form)


@app.route("/search", methods=["GET", "POST"])
def search():
    form = Search()
    if form.validate_on_submit():
        location = form.location.data
        result = db.session.query(Cafe).filter(Cafe.location == location)
        return render_template('search.html', form=form, cafes=result)
    return render_template('search.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
