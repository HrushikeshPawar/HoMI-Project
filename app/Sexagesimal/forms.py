from flask_wtf import FlaskForm
from wtforms.fields import StringField, BooleanField, SubmitField, IntegerField, RadioField, DecimalField
from wtforms.validators  import DataRequired, InputRequired

class D2S_Form(FlaskForm):

    Decimal = DecimalField('Decimal', validators=[DataRequired()], places=1000)
    Fractions = IntegerField('Fractions')
    D2S_Submit = SubmitField('Convert')
    Reset = SubmitField('Reset')
    

class S2D_Form(FlaskForm):

    Sexagesimal = StringField('Sexagesimal', validators=[DataRequired()])
    Precision = IntegerField('Precision')
    S2D_Submit = SubmitField('Convert')
    

class Addition_Subtraction_Form(FlaskForm):

    AddSub_Input = StringField('Input', validators=[DataRequired()])
    Verbose = BooleanField('Verbose')
    AddSub_Submit = SubmitField('Calculate')
    

class Multiplication_Form(FlaskForm):

    Mul_Input = StringField('Input', validators=[DataRequired()])
    Verbose = BooleanField('Verbose')
    Mul_Submit = SubmitField('Calculate')
    

class Division_Form(FlaskForm):

    Dividend = StringField('Dividend', validators=[DataRequired()])
    Divisor = StringField('Divisor', validators=[DataRequired()])
    Precision = IntegerField('Divisor')
    Choices = RadioField('Options', choices=[('Normal', 'Normal'), ('Advance', 'Advanve'), ('Verbose', 'Verbose')], default='Normal')
    Div_Submit = SubmitField('Calculate')
    

class Increment_Table_Form(FlaskForm):

    Initial_Value = StringField('Initial Value', validators=[DataRequired()])
    Increment_Value = StringField('Increment Value', validators=[InputRequired()])
    Rows = IntegerField('Rows', validators=[InputRequired()])
    Output_Mod = IntegerField('Output Mod')
    ITF_Submit = SubmitField('Calculate')
    