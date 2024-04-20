from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ------- Connect to DB -------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# ----- Cafe TABLE Configuration -----

class Cafe(db.Model):
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


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/all')
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.convert_to_dict() for cafe in all_cafes])


if __name__ == '__main__':
    app.run(debug=True)
