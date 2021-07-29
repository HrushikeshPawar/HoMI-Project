from flask import Blueprint, render_template, redirect, url_for, request
from .Sexagesimal import Sexagesimal
from .forms import D2S_Form, S2D_Form, Addition_Subtraction_Form, Multiplication_Form, Division_Form, Increment_Table_Form
from .utils import isValidInput, Addition, Multiplication,  MultiAdvance, Division, DiviAdvance, Integral2Decimal, getOutputs

sexagesimal_new = Blueprint('sexagesimal_new', __name__, static_folder='/static', template_folder='templates')

@sexagesimal_new.route('/sexagesimal-calculator-new', methods=['POST', 'GET'])
def Calculator_New():

    D2S_form = D2S_Form()
    S2D_form = S2D_Form()
    Addition_Subtraction_form = Addition_Subtraction_Form()
    Multiplication_form = Multiplication_Form()
    Division_form = Division_Form()
    Increment_Table_form = Increment_Table_Form()
    scroll = ''

    Outputs = getOutputs(request.form)
    D2S_Output     =   Outputs['Dec2Sexa_output']
    S2D_Output     =   Outputs['Sexa2Dec_output']
    AddSub_output       =   Outputs['AddSub_output']
    Mul_output          =   Outputs['Mul_output']
    Div_output          =   Outputs['Div_output']
    Inc_output          =   Outputs['Inc_output']
    print(D2S_Output,S2D_Output, request.form)

    if D2S_form.D2S_Submit.data:
        scroll = 'D2S'

        Decimal = str(D2S_form.Decimal.data)
        if D2S_form.Fractions.data:
            Fraction = D2S_form.Fractions.data
        else:
            Fraction = ''
        try:
            if isValidInput(Decimal):
                Decimal = Decimal.replace(' ', '')

                if Decimal[0] == '.':
                    Decimal = '0' + Decimal

                if Fraction == '':
                    D2S_Output = Sexagesimal.decimal2Sexagesimal(Decimal)
                else:
                    D2S_Output = Sexagesimal.decimal2Sexagesimal(Decimal, Accuracy=int(Fraction))
            else:
                D2S_Output = "Invalid Input"
        except:
            D2S_Output = "Invalid Input"
        
        return render_template('sexagesimal-calculator-new.html', D2S_Form=D2S_form, S2D_form=S2D_form, 
                            Addition_Subtraction_form=Addition_Subtraction_form, Multiplication_form=Multiplication_form,
                            Division_form=Division_form, Increment_Table_form=Increment_Table_form, D2S_Output=D2S_Output)
    
    if S2D_form.S2D_Submit.data:
        scroll = 'S2D'
        Sexagesimal_Input = S2D_form.Sexagesimal.data
        if S2D_form.Precision.data:
            Precision = S2D_form.Precision.data
        else:
            Precision = ''
        
        try:
            if isValidInput(Sexagesimal_Input):
                if Precision == "":
                    S2D_Output = Sexagesimal.Sexagesimal2Decimal(Sexagesimal_Input)
                else:
                    S2D_Output = Sexagesimal.Sexagesimal2Decimal(Sexagesimal_Input, precision=int(Precision))
            else:
                S2D_Output = "Invalid Input"
        except:
            S2D_Output = "Invalid Input"

        return render_template('sexagesimal-calculator-new.html', D2S_Form=D2S_form, S2D_form=S2D_form, 
                            Addition_Subtraction_form=Addition_Subtraction_form, Multiplication_form=Multiplication_form,
                            Division_form=Division_form, Increment_Table_form=Increment_Table_form, D2S_Output=D2S_Output,
                            S2D_Output=S2D_Output)
            
    

    return render_template('sexagesimal-calculator-new.html', D2S_Form=D2S_form, S2D_form=S2D_form, 
                            Addition_Subtraction_form=Addition_Subtraction_form, Multiplication_form=Multiplication_form,
                            Division_form=Division_form, Increment_Table_form=Increment_Table_form)



