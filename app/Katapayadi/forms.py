from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators  import DataRequired, InputRequired

class KatapayadiDecoder(FlaskForm):

    Input = StringField('Input', validators=[DataRequired('Input Required')])
    Encoding = SelectField('Encoding', choices=["SLP1", "Devanagari", "IAST", "ITRANS", "HK", "Kolkata", "Kannada", "Malayalam", "Telugu"])
    Verbose = BooleanField('Verbose')
    Submit = SubmitField('Submit')

class KatapayadiEncoder(FlaskForm):

    Input = IntegerField('Number', validators=[InputRequired('Input Required')])
    Options = IntegerField('Options', validators=[InputRequired('Input Required')])
    Submit = SubmitField('Submit')