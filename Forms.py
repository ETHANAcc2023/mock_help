from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, HiddenField, TextAreaField
from wtforms.validators  import EqualTo, data_required

# Using WTFforms to create a sign in form
class Sign_in_form(FlaskForm):
    username = StringField(validators=[data_required()], render_kw={"placeholder": "Username"})
    email = StringField(validators=[data_required()], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[data_required()], render_kw={"placeholder": "Password"})
    submit = SubmitField()

# Using WTFforms to create a sign up form
class Sign_up_form(FlaskForm):
    username = StringField(validators=[data_required()], render_kw={"placeholder": "Username"})
    email = StringField(validators=[data_required()], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[data_required(), EqualTo('confirm_password')], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField(validators=[data_required()], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField()

# Using WTFforms to create a Form that lets users create posts 
class Postform(FlaskForm):
    Title = StringField(validators=[data_required()], render_kw={"placeholder": "Title"})
    Content = TextAreaField(validators=[data_required()], render_kw={"placeholder": "Content"})
    submit = SubmitField()