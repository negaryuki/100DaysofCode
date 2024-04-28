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


@app.route('/all')
def get_all_cafes():
    all_cafes = Cafe.query.order_by(Cafe.name).all()
    return render_template('all_cafe.html', all_cafes=[cafe.convert_to_dict() for cafe in all_cafes])

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template("signup.html", form=form)

@app.route("/search")
def search_cafe_with_location():
    location_query = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location_query))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.convert_to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have any cafes in that area "})


if __name__ == '__main__':
    app.run(debug=True)
