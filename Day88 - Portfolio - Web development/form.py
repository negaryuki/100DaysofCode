from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL

class CafeForm (FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField("Cafe Location")
    open = StringField ("Opening Time", validators=[DataRequired()])
    close = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField("Coffe Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪","💪💪", "💪💪" ])


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password")
    submit = SubmitField('Sign Up')