from wtforms import TextAreaField, SubmitField, DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class DateForm(FlaskForm):
    date_info = TextAreaField('Date', validators=[DataRequired()])
    submit_date = SubmitField('Submit Date')


class ToDoForm(FlaskForm):
    todo_info = TextAreaField('Add Task', validators=[DataRequired()])
    submit_todo = SubmitField('Submit Task')
