from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Optional


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField("Email", validators=[Email(), DataRequired()])
    phone_number = StringField("Phone", validators=[Optional()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Submit")
