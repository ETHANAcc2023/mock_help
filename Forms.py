from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, HiddenField
from wtforms.validators  import EqualTo, data_required

# Using WTFforms to create a sign in form
class Sign_in_form(FlaskForm):
    username = StringField("Username:",validators=[data_required()])
    email = StringField("Email:",validators=[data_required()])
    password = PasswordField("Password:",validators=[data_required()])
    submit = SubmitField()

# Using WTFforms to create a sign up form
class Sign_up_form(FlaskForm):
    username = StringField("Username:",validators=[data_required()])
    email = StringField("Email:",validators=[data_required()])
    password = PasswordField("Password:",validators=[data_required(), EqualTo('confirm_password')])
    confirm_password = PasswordField("Confirm Password:", validators=[data_required()])
    submit = SubmitField()

# Using WTFforms to create a Form that lets users create posts 
class Postform(FlaskForm):
    Title = StringField("Title:",validators=[data_required()])
    Content = StringField("Content:",validators=[data_required()])
    submit = SubmitField()