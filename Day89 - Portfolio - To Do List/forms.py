from wtforms import BooleanField, SubmitField, StringField, DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


# Define the WTForms task form
class TaskForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    description = StringField("Task", validators=[DataRequired()])
    completed = BooleanField('Completed')
    submit = SubmitField('Submit')



class DateForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])
