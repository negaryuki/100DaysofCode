from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField("Cafe Location")
    open = StringField("Opening Time", validators=[DataRequired()])
    close = StringField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField("Coffe Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪"])
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                               validators=[DataRequired()])
    submit = SubmitField('Submit')


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password")
    submit = SubmitField('Sign Up')


class CafeSortForm(FlaskForm):
    sort_by = SelectField('Sort By', choices=[
        ('id', 'ID'),
        ('name', 'Name'),
        ('location', 'Location'),
        ('seats', 'Seats'),
        ('coffee_price', 'Coffee Price')
    ])

class Search(FlaskForm):
    location = StringField("Location", validators=[DataRequired()])
    submit = SubmitField("Search")