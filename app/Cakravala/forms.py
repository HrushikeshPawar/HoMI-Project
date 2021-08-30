from flask_wtf import FlaskForm
from wtforms.fields import  BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators  import DataRequired, InputRequired, ValidationError

def check_integer(form, field):
    try:
        int(field.data)
    except:
        print(field)
        raise ValidationError('Field must contain only integer value')
class CakravalaForm(FlaskForm):

    Input = IntegerField('Input', validators=[InputRequired('Input Required'), DataRequired()])
    Algorithm = SelectField('Algorithm', choices=['Chakravala - (By Bhaskara II)', "Lagrange's Method to solve Pell's Equation", "Chakravala with Bhramhaguta's Shortcuts"])
    Verbose = BooleanField('Verbose')
    Submit = SubmitField('Submit')
