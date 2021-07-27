from wtforms.validators import InputRequired
from .Sexagesimal import Sexagesimal


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
        #print(f"\nA\t=\t{A}")
        #print(f"B\t=\t{B}")
        Details += f"\nA\t=\t{A}"
        Details += f"\nB\t=\t{B}"
        
    # Step1 : Get the Rational Form of B
    try:
        B_Num, B_Denom = str(Sexagesimal.getRationlForm(B)).split("/")
    except:
        B_Num = str(Sexagesimal.getRationlForm(B))
        B_Denom = 1

    if Verbose:
        #print(f"\n\n\nStep 1: Get the rational form of B")
        #print(f"\n\tB\t=\t {B_Num}")
        #print(f"\t \t \t{'-' * (len(B_Num)+2)}")
        #print(f"\t \t \t {B_Denom}")
        Details += f"\n\n\n\nStep 1: Get the rational form of B"
        Details += f"\n\n\tB\t=\t {B_Num}"
        Details += f"\n\t \t \t{'_' * (len(B_Num)+2)}"
        Details += f"\n\t \t \t {B_Denom}"
        
    
    # Step 2: Get Reciprocal of the B_Num
    B_Num_R, Recur, flag = Sexagesimal.getReciprocal(int(B_Num), Precision+10)
    B_Num_R1 = Sexagesimal(B_Num_R)

    if Verbose:
        #print(f"\n\n\nStep 2: Get the reciprocal of the numberator of B (Why? Because, dividing by B is same as multiplying by reciprocal of B)")
        Details += f"\n\n\n\nStep 2: Get the reciprocal of the numberator of B (Why? Because, dividing by B is same as multiplying by reciprocal of B)"
        if flag:
            #print(f"\n\tThe numerator of B is not a regular number (i.e has a prime factor other than 2, 3 or 5).")
            #print(f"\tHence, the reciprocal of numberator is non-terminating but recurring! (The recurring term is enclosed on brackets)")
            Details += f"\n\n\tThe numerator of B is not a regular number (i.e has a prime factor other than 2, 3 or 5)."
            Details += f"\n\tHence, the reciprocal of numberator is non-terminating but recurring! (The recurring term is enclosed on brackets)"
        else:
            #print(f"\n\tThe numerator of B is a regular number. Hence, the reciprocal has an exact Sexagesimal Representation")
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
        #print(f"\n\n\nStep 3: Calculate the Reciprocal of B (Denominator x Reciprocal of Numerator)")
        #print(f"\n\tReciprocal of B (B')\t=\t{B_R}")
        Details += f"\n\n\n\nStep 3: Calculate the Reciprocal of B (Denominator x Reciprocal of Numerator)"
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
        #print(f"\n\n\nStpe 4: Do the actual Division (A/B = A * B')")
        #print(f"\n\tA/B\t=\t{Div}")
        Details += f"\n\n\n\nStpe 4: Do the actual Division (A/B = A * B')"
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

            #print(f"\n\nThe above answer of division (A/B) when again multiplied with B gives A correctly upto {cnt} Sexagesimal places in the fraction part\n")
            #print(f"\n\tA'\t=\tA/B * B\t=\t{A_New}\n\n")
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
