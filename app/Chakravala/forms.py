from flask_wtf import FlaskForm
from wtforms.fields import  BooleanField, SubmitField, IntegerField
from wtforms.validators  import DataRequired, InputRequired


class ChakravalaForm(FlaskForm):

    Input = IntegerField('Input', validators=[InputRequired('Input Required'), DataRequired()])
    Verbose = BooleanField('Verbose')
    Submit = SubmitField('Submit')
