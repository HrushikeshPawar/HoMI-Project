from flask import Flask, render_template, request, Blueprint
from .Sexagesimal import Sexagesimal

sexagesimal = Blueprint('sexagesimal', __name__, static_folder='/static', template_folder='templates')

@sexagesimal.route('/sexagesimal-calculator', methods=['POST', 'GET'])
def Calculator():
    
    mkd_text = '''### 1. Decimal to Sexagesimal Converter\n- Input should be decimal number.
    - Allowed inputs - 1, 0.23, .23, 1.0
    - **Fraction** (optional) : 
        - The number of digits to consider after the decimal point.
        -  Example : If input is 1.23456 and fraction is 2, then the program will consider only 1.23 for conversion.

    ---

    ### 2. Sexagesimal to Decimal Converter:
    - Input should be a sexagesimal number.
    - ' ; ' should be used to separat the intergal part 
    - ' , ' should be used to separate the fractional apart.
    - Example : 12;01,45,12
    - **Precision** (optional) :
        - Number of fractional places to consider in the final result.
        - Examples: 
            - 21;19,53,47,43,29  --->  21.33160983667695473251 (20 decimal places). 
            - But if Precision value is 30, then the result will be 21.331609836676954732510288065844
        - By default, the program will give result till 20 decimal places.
        - This option is helpful if the given sexagesimal number contains a non-regular number in the fractional part.

    ---

    ### 3. Addition and Subtraction:
    - Input can be in the decimal form, sexagesimal form or mixed.
    - But the answer will always be in the sexagesimal form
    - Example :
        - 1.23 + 4.32 - 5.32  = 00;13,48
        - 4;2,45 + 6;12,1 - 1,45;12,56,78 = -01,34;58,11,18
        - 1.23 + 4.32 - 1,45;12,56,78 = -01,39;39,57,18

    ---

    ### 4. Multiplication:
    - Input can be in the decimal form, sexagesimal form or mixed.
    - But the answer will always be in the sexagesimal form
    - Example :
        - 1.23 * - 5.32  = -06;32,36,57,36
        - (-4;2,45) * (-6;12,1) = 25;05,07,02,45
        - -4.32 * 1,45;12,56,78 = -07,34;31,57,56,09,36
    - **Verbose** (Optional):
        - When selected the program will print every step involved in the calculation.
        - This can be used to check the steps and confirm the correctness.
        - It also shows that all the intermediate calculations are done in sexagesimal number system and there is no back and forth from the decimal system.

    ---

    ### 5. Division:
    - The inputs (Dividend and Divisor) can be decimal, sexagesimal or mixed.
    - But the answer will always be in the sexagesimal form.
    Example : 
        - 3.24 / 6.12 = 00;31,45,52,56,28,14,07,03,31,45,52,56,28,14,07,03,31,45,52,56
        - 03;14,24 / 06;07,12 = 00;31,45,52,56,28,14,07,03,31,45,52,56,28,14,07,03,31,45,52,56
        - 3.24 / 6;04 = 00;31,45,52,56,28,14,07,03,31,45,52,56,28,14,07,03,31,45,52,56
    - **Precision** :
        - By default, the program prints final answer upto 20 fractional places.
        - This option could be used to increase or decrease the number of fractional places to be displayed in the final answer.
    - **Verbose** :
        - When selected the program will print every step involved in the calculation.
        - This can be used to check the steps and confirm the correctness.

    ---

    ### 6. Increment Table Generator:
    - Used to create the addition and subtraction tables.
    - The Initial value and the Increment value can be in decimal, sexagesimal or mixed form.
    - The Row and Mod has to be a positive integer.
    - If Row is empty then default value (10) will be consider.
    - If mod is empty or less than 2, then the integral part of values will be a decimal and will not be moded.


    '''

    # Get the inputs
    Inputs = getInputs(request.form)
    Dec2Sexa_Decimal        =   Inputs['Dec2Sexa_Decimal']
    Dec2Sexa_Fraction       =   Inputs['Dec2Sexa_Fraction']
    Sexa2Dec_Sexagesimal    =   Inputs['Sexa2Dec_Sexagesimal']
    Sexa2Dec_Precision      =   Inputs['Sexa2Dec_Precision']
    AddSub_Input            =   Inputs['AddSub_Input']
    Mul_Input               =   Inputs['Mul_Input']
    Mul_Verbose             =   Inputs['Mul_Verbose']
    Div_Dividend            =   Inputs['Div_Dividend']
    Div_Divisor             =   Inputs['Div_Divisor']
    Div_Set_Precision       =   Inputs['Div_Set_Precision']
    Div_Radio               =   Inputs['Div_Radio']
    Inc_Initial             =   Inputs['Inc_Initial']
    Inc_Increment           =   Inputs['Inc_Increment']
    Inc_Rows                =   Inputs['Inc_Rows']
    Inc_Mod                 =   Inputs['Inc_Mod']
    scroll                  =   ''

    # Initialize the Outputs
    Outputs = getOutputs(request.form)
    Dec2Sexa_output     =   Outputs['Dec2Sexa_output']
    Sexa2Dec_output     =   Outputs['Sexa2Dec_output']
    AddSub_output       =   Outputs['AddSub_output']
    Mul_output          =   Outputs['Mul_output']
    Div_output          =   Outputs['Div_output']
    Inc_output          =   Outputs['Inc_output']


    if 'Dec2Sexa_Decimal' in request.form:
        try:
            if request.form['btn-Dec2Sexa'] == 'Convert':
                scroll = 'D2S'
                try:
                    if isValidInput(Dec2Sexa_Decimal):
                        Dec2Sexa_Decimal = Dec2Sexa_Decimal.replace(' ', '')

                        if Dec2Sexa_Decimal[0] == '.':
                            Dec2Sexa_Decimal = '0' + Dec2Sexa_Decimal

                        if Dec2Sexa_Fraction == '':
                            Dec2Sexa_output = Sexagesimal.decimal2Sexagesimal(Dec2Sexa_Decimal)
                        else:
                            Dec2Sexa_output = Sexagesimal.decimal2Sexagesimal(Dec2Sexa_Decimal, Accuracy=int(Dec2Sexa_Fraction))
                    else:
                        Dec2Sexa_output = "Invalid Input"
                except:
                    Dec2Sexa_output = "Invalid Input"
            
            else:
                scroll = 'D2S'
                Dec2Sexa_output = ''
                Dec2Sexa_Decimal = ''
                Dec2Sexa_Fraction = ''

        except:
            pass
    
    if 'Sexa2Dec_Sexagesimal' in request.form:
        
        try:
            if request.form['btn-Sexa2Dec'] == 'Convert':
                scroll = 'S2D'
                try:
                    if isValidInput(Sexa2Dec_Sexagesimal):
                        if Sexa2Dec_Precision == "":
                            Sexa2Dec_output = Sexagesimal.Sexagesimal2Decimal(Sexa2Dec_Sexagesimal)
                        else:
                            Sexa2Dec_output = Sexagesimal.Sexagesimal2Decimal(Sexa2Dec_Sexagesimal, precision=int(Sexa2Dec_Precision))
                    else:
                        Sexa2Dec_output = "Invalid Input"
                except:
                    Sexa2Dec_output = "Invalid Input"
            
            else:
                scroll = 'S2D'
                Sexa2Dec_output = ''
                Sexa2Dec_Sexagesimal = ''
                Sexa2Dec_Precision = ''
                print(Exception)
            
        except:
            pass
    
    if 'AddSub_Input' in request.form:

        try:
            if request.form['btn-AddSub'] == 'Calculate':
                scroll = 'addition-subtraction'
                AddSub_output = Addition(AddSub_Input)
            else:
                AddSub_Input = ''
                AddSub_output = ''
                scroll = 'addition-subtraction'

        except Exception as e:
            print(e)
 
    if 'Mul_Input' in request.form:
        
        try:
            if 'btn-Mul' in request.form:
                scroll = 'multiplication'
                if request.form['btn-Mul'] == 'Calculate':

                    Mul_Input = Mul_Input.replace(' ', '')


                    if Mul_Verbose == 'on':
                        Mul_output = MultiAdvance(Mul_Input)
                    else:
                        Mul_output = Multiplication(Mul_Input)
                    
                else:
                    Mul_Input = ''
                    Mul_output = ''
                    Mul_Verbose = None
        except Exception as e:
            print(e)
            print('Invalid Input')
    
    if 'Div_Dividend' in request.form and 'Div_Divisor' in request.form:
        
        try:
            if 'btn-Div' in request.form:
                scroll = 'division'
                if request.form['btn-Div'] == 'Calculate':

                    if Div_Set_Precision == '':
                        Div_Set_Precision = 20

                    if Div_Radio == 'Div_Normal':
                        Div_output = Division(Div_Dividend, Div_Divisor)
                    elif Div_Radio == 'Div_Precision':
                        Div_output = DiviAdvance(Div_Dividend, Div_Divisor, Precision=int(Div_Set_Precision), Verbose=False)
                    else:
                        Div_output = DiviAdvance(Div_Dividend, Div_Divisor, Precision=int(Div_Set_Precision), Verbose=True)
                    
                else:
                    Div_Dividend        =   ''
                    Div_Divisor         =   ''
                    Div_Set_Precision   =   ''

        except Exception as e:
            print(e)
            Div_output = 'Invalid Input'

    if 'Inc_Initial' in request.form:
        
        try:
            if 'btn-Inc' in request.form:
                
                scroll = 'increment'
                if request.form['btn-Inc'] == "Calculate":
                    Inputs = [Inc_Initial, Inc_Increment]
                    flag = 0
                    for Input in Inputs:

                        if not isValidInput(Input):
                            flag = 1
                            break
                    
                    for i in range(len(Inputs)):
                        if '.' in Inputs[i]:
                            Inputs[i] = Sexagesimal.decimal2Sexagesimal(Inputs[i].strip())
                        else:
                            Inputs[i] = Sexagesimal(Inputs[i].strip())

                    Inc_Initial, Inc_Increment = Inputs
                    try:
                        Inc_Rows = int(Inc_Rows)
                        Inc_Mod = int(Inc_Mod)
                    except:
                        if type(Inc_Rows) == type(1) and Inc_Mod == '':
                            Inc_Rows = int(Inc_Rows)
                            Inc_Mod = 0
                        else:
                            flag = 1
                    
                    if flag == 0:
                        if Inc_Mod < 2 or Inc_Mod == '':
                            Inc_Mod = 0
                    
                        A = Sexagesimal(Inc_Initial)
                        i=0
                        Inc_output = []

                        if A.negative:
                            Inc_output.append(f'-{A.S}')
                        else:
                            Inc_output.append(A.S)
                        
                        while i < Inc_Rows:

                            B = Sexagesimal(Inc_Increment)
                            A = A + B
                            
                            A_I = Integral2Decimal(A)
                            A_D, A_F = A_I.split(";")
                            
                            if Inc_Mod == 0:
                                
                                if A.negative == True and A.S != "00;00":
                                    A = Sexagesimal(f"-{A_D};{A_F}")
                                    Inc_output.appned(f"-{Integral2Decimal(A)}")
                                    
                                else:
                                    A = Sexagesimal(f"{A_D};{A_F}")
                                    Inc_output.append(f"{Integral2Decimal(A)}")
                                    
                            else:
                                A_D = int(A_D) % Inc_Mod

                                if A.negative == True and A.S != "00;00":
                                    A = Sexagesimal(f"-{A_D};{A_F}")
                                    if Inc_Mod > 60:
                                        Inc_output.append(f"-{Integral2Decimal(A)}")
                                    else:
                                        Inc_output.append(f"-{A.S}")
                                else:
                                    A = Sexagesimal(f"{A_D};{A_F}")
                                    if Inc_Mod > 60:
                                        Inc_output.append(f"{Integral2Decimal(A)}")
                                    else:
                                        Inc_output.append(f"{A.S}")

                            
                            i += 1
                    else:
                        Inc_output = "Invalid Input"

                    if Inc_Mod == 0:
                        Inc_Mod = ''
                else:
                    Inc_Initial = ''
                    Inc_Increment = ''
                    Inc_Rows = ''
                    Inc_Mod = ''
                    Inc_output = ''
        except Exception as e:
            print(e)
            Inc_output = "Invalid Input"


    try:
        return render_template(f'sexagesimal-calculator.html', Dec2Sexa_output=Dec2Sexa_output, Dec2Sexa_Decimal=Dec2Sexa_Decimal, Dec2Sexa_Fraction=Dec2Sexa_Fraction
                                        ,   Sexa2Dec_output=Sexa2Dec_output, Sexa2Dec_Sexagesimal=Sexa2Dec_Sexagesimal, Sexa2Dec_Precision=Sexa2Dec_Precision
                                        ,   AddSub_output=AddSub_output, AddSub_Input=AddSub_Input
                                        ,   Mul_Input=Mul_Input, Mul_output=Mul_output, Mul_Verbose=Mul_Verbose
                                        ,   Div_Dividend=Div_Dividend, Div_Divisor=Div_Divisor, Div_Set_Precision=Div_Set_Precision
                                        ,   Div_output=Div_output, Inc_Increment=Inc_Increment, Inc_Initial=Inc_Initial
                                        ,   Inc_Mod=Inc_Mod, Inc_Rows=Inc_Rows, Inc_output=Inc_output, scroll=scroll, mkd_text=mkd_text
                                        ,   title='Sexagesimal')
    except:
        return render_template('sexagesimal-calculator.html',   title='Sexagesimal')

# Helping Functions

def isValidInput(Input):

    Input = Input.strip()

    signs = ['+', '-', '*', '/', '(', ')', '[', ']', '{', '}', ' ']
    for Input in Input:
        for sign in signs:
            Input = Input.replace(sign, '')

    if Input.isdigit():
        return True

    if "." in Input and Input.count(".") > 1:
        return False
    
    if "." in Input:
        return Input.replace('.', '').isdigit()
    
    if ',' in Input and ';' not in Input:
        return False
    
    if ';' in Input:
        Input = Input.replace(",", '')
        return Input.replace(';', '').isdigit()
    
    print(Input)

def getInputs(Data):
    Inputs = ['Dec2Sexa_Decimal', 'Dec2Sexa_Fraction', 'Sexa2Dec_Sexagesimal', 'Sexa2Dec_Precision', 'AddSub_Input'
            , 'Mul_Input', 'Mul_Verbose', 'Div_Dividend', 'Div_Divisor', 'Div_Radio', 'Div_Set_Precision'
            ,   'Inc_Initial', 'Inc_Increment', 'Inc_Rows', 'Inc_Mod']
    Values = dict()

    for Input in Inputs:

        try:
            if Data.get(Input) == None:
                Values[Input] = ''
            else:
                Values[Input] = Data.get(Input)
        except:
            Values[Input] = ''

    return Values

def getOutputs(Data):

    Outputs = ['Dec2Sexa_output', 'Sexa2Dec_output', 'AddSub_output', 'Mul_output', 'Div_output', 'Inc_output']
    Values = dict()

    for output in Outputs:
        
        try:
            if Data.get(output) == None:
                Values[output] = ''
            else:
                Values[output] = Data.get(output)
        except:
            Values[output] = ''
    return Values

def Addition(Input):

    Signs = ['+', '-']
    Operations = []
    Input = list(Input)

    flag = 0
    for i in range(len(Input)):
        if Input[i] in Signs and i!=0:
            flag = 1
            Operations.append(Input[i])
            Input[i] = ' '
    
    if flag == 0:
        return "Invalid Input"

    Input = ''.join(Input)
    Numbers = Input.split()

    for n in Numbers:
        if not isValidInput(n):
            return "Invalid Input"
    
    for i in range(len(Numbers)):

        if '.' in Numbers[i]:
            Numbers[i] = Sexagesimal.decimal2Sexagesimal(Numbers[i].strip())
        else:
            Numbers[i] = Sexagesimal(Numbers[i].strip())

    Result = Numbers[0]

    for i in range(len(Numbers) - 1):

        if Operations[i] == '+':
            Result += Numbers[i+1]
        
        elif Operations[i] == '-':
            Result -= Numbers[i+1]
        
        else:
            return "Invalid Input"
    
    return Result

def Multiplication(Input):
    
    if "(" in Input:
        Input = Input.replace("(", "")
    if ")" in Input:
        Input = Input.replace(")", "")
        
    Input = Input.split("*")
    print(Input)
    for n in Input:
        if not isValidInput(n):
            return "Invalid Input"
    
    for i in range(len(Input)):

        if '.' in Input[i]:
            Input[i] = Sexagesimal.decimal2Sexagesimal(Input[i].strip())
        else:
            Input[i] = Sexagesimal(Input[i].strip())
    A = Input[0]

    print(Input)
    
    i = 1
    while i < len(Input):
        B = Input[i]
        A = A * B
        i += 1
        
    if A.negative:
        return f"-{A.S}"
    
    return A.S

def MultiAdvance(Input):
    
    if "(" in Input:
        Input = Input.replace("(", "")
    if ")" in Input:
        Input = Input.replace(")", "")
    
    Input = Input.split("*")

    
    for n in Input:
        if not isValidInput(n):
            return "Invalid Input"
    

    for i in range(len(Input)):

        if '.' in Input[i]:
            Input[i] = Sexagesimal.decimal2Sexagesimal(Input[i].strip())
        else:
            Input[i] = Sexagesimal(Input[i].strip())
    
    A = Input[0]
    
    i = 1
    Details = ""
    while i < len(Input):
        B = Input[i]
        
        A, res = Sexagesimal.Multiplication(A, B)
        Details += res
        i += 1
        
    return Details.strip() 

def Division(Dividend, Divisor):

    Input = [Dividend, Divisor]

    for n in Input:
        if not isValidInput(n):
            return "Invalid Input"
    

    for i in range(len(Input)):

        if '.' in Input[i]:
            Input[i] = Sexagesimal.decimal2Sexagesimal(Input[i].strip())
        else:
            Input[i] = Sexagesimal(Input[i].strip())
    
    Div = Input[0] / Input[1]

    if Div.negative:
        return f"-{Div.S}"
    else:
        return Div.S

def DiviAdvance(A, B, Precision=20, Verbose=False):

    # Get A and B as right form of Sexagesimal string
    Input = [A, B]
    for i in range(len(Input)):
        if '.' in Input[i]:
            Input[i] = Sexagesimal.decimal2Sexagesimal(Input[i].strip())
        else:
            Input[i] = Sexagesimal(Input[i].strip())

    A, B = Input

    try:
        A_S = A.S
        B_S = B.S
    except:
        A = Sexagesimal(A)
        B = Sexagesimal(B)
        A_S = A.S
        B_S = B.S
    
    Details = ""
    
    # Print the above details
    if Verbose:
        Details = f"\n\n\n\n**Inputs:**"
        Details += f"\n\n\tA\t=\t{A}"
        Details += f"\n\tB\t=\t{B}"
        
    # Step1 : Get the Rational Form of B
    try:
        B_Num, B_Denom = str(Sexagesimal.getRationlForm(B)).split("/")
    except:
        B_Num = str(Sexagesimal.getRationlForm(B))
        B_Denom = 1

    if Verbose:
        Details += f"\n\n\n\n**Step 1:** Get the rational form of B"
        Details += f"\n\n\tB\t=\t {B_Num}"
        Details += f"\n\t \t \t{'-' * (len(B_Num)+2)}"
        Details += f"\n\t \t \t {B_Denom}"
        
    
    # Step 2: Get Reciprocal of the B_Num
    B_Num_R, Recur, flag = Sexagesimal.getReciprocal(int(B_Num), Precision+10)
    B_Num_R1 = Sexagesimal(B_Num_R)

    if Verbose:
        
        Details += f"\n\n\n\n**Step 2:** Get the reciprocal of the numberator of B (Why? Because, dividing by B is same as multiplying by reciprocal of B)"
        if flag:
            Details += f"\n\n\tThe numerator of B is not a regular number (i.e has a prime factor other than 2, 3 or 5)."
            Details += f"\n\tHence, the reciprocal of numberator is non-terminating but recurring! (The recurring term is enclosed on brackets)"
        else:
            Details += f"\n\n\tThe numerator of B is a regular number. Hence, the reciprocal has an exact Sexagesimal Representation"
        
        if len(Recur) == 0:

            try:
                n = len(B_Num_R.split(";")[1].split(","))
            except:
                n = len(B_Num_R.S.split(";")[1].split(","))

            if n > Precision:
                B_Num_R = Sexagesimal.RoundOff(B_Num_R, Precision)
        
            Details += f"\n\n\tReciprocal of numerator {B_Num}\t=\t{B_Num_R}"
        else:
            Details += f"\n\n\tReciprocal of numerator {B_Num}\t=\t{Recur}"


    # Step 3: Now we get the Reciprocal of B
    B_Denom = Sexagesimal(B_Denom)
    B_R = B_Num_R1 * B_Denom        
    if Verbose:
        Details += f"\n\n\n\n**Step 3:** Calculate the Reciprocal of B (Denominator x Reciprocal of Numerator)"
        print(B_R)
        X = Sexagesimal.RoundOff(B_R, Precision)
        Details += f"\n\n\tReciprocal of B (B')\t=\t{X}"       

    # Step 4: And now we do the actual divison. Which is nothing but multiplication with the reciprocal
    Div = A * B_R
    if A.negative and B.negative == False:
        Div.negative = True
    elif A.negative == False and B.negative:
        Div.negative = True
    else:
        Div.negative = False
    
    if len(Div.S.split(";")[1].split(",")) > Precision:
            Div = Sexagesimal.RoundOff(Div, Precision)            

    if Verbose:
        Details += f"\n\n\n\n**Stpe 4:** Do the actual Division (A/B = A * B')"
        Details += f"\n\n\tA/B\t=\t{Div}"

        if flag:

            A_D, A_F = A.S.split(";")
            A_D = A_D.split(",")
            A_F = A_F.split(",")
            
            A_New = Div * B
            A_New_D, A_New_F = A_New.S.split(";")
            A_New_D = A_New_D.split(",")
            A_New_F = A_New_F.split(",")

            cnt = 0
            for i in range(len(A_F)):

                if A_F[i] != A_New_F[i]:
                    break
                else:
                    cnt += 1

            Details += f"\n\n\nThe above answer of division (A/B) when again multiplied with B gives A correctly upto {cnt} Sexagesimal places in the fraction part\n"
            Details += f"\n\n\tA'\t=\tA/B * B\t=\t{A_New}\n\n"      
        
    if Verbose:
        return Details
    else:
        return f"{Div}"

def Integral2Decimal(Input):
    
    A_D, A_F = Input.S.split(";")
    A_D = A_D.split(",")
    
    Dec = 0
    for i in range(len(A_D)):
        
        Dec += int(A_D[-(i+1)]) * (60 ** i)
    
    return f"{Dec};{A_F}"
