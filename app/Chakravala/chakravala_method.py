from flask import Blueprint, render_template
from .forms import ChakravalaForm
from .Chakravala import chakravala, samasabhavana
from math import sqrt

Chakravala = Blueprint('Chakravala', __name__, static_folder='static', template_folder='templates')

@Chakravala.route('/chakravala-calculator', methods=['POST', 'GET'])
def chakravala_method():

    form = ChakravalaForm()

    if form.validate_on_submit():

        n = form.Input.data
        verbose = form.Verbose.data

        if n>1 and int(sqrt(n))!=sqrt(n) and int(n)==n:
        
            iteration = chakravala(n)
            error = False

            text = f'''\n We use chakravala to solve for a<sup>2</sup> = {n}b<sup>2</sup> + 1.
            
            \n Begin with the general equation a<sup>2</sup> = {n}b<sup>2</sup> + m and apply chakravala till m equals 1.
            
            \nFor n = {n}, we need {len(iteration)} iterations to arrive at an answer.

            \nThe smallest integer solution for a<sup>2</sup> = {n}b<sup>2</sup> + 1 
            
            a = {iteration[-1][0]} and b = {iteration[-1][1]}.
            '''

            """
            m=int(input("\nEnter the number of solutions needed:"))
            if m<1:
                print("Invalid Input")
            else:  
                print(f"\n")
                sol_list=samasabhavana(n,p,q,m)

                i=1
                for x in sol_list:
                    print(f"{i}. {x}")
                    p,q=x
                    print(f"   Check output {p}**2-({n}*({q}**2))={p**2-(n*(q**2))}\n")
                    i=i+1    
            """
            """
            elif int(n)!=n and n<=1:
                #print("\nInvalid input. The input is not an integer and is <=1.")
                error = True
            elif int(sqrt(n))==sqrt(n) and n<=1:
                #print("\nInvalid input. The input is a perfect square and is<=1.")
                error = True
            elif int(sqrt(n))==sqrt(n):
                #print("\nInvalid input. The input is a perfect square.")
                error = True
            elif int(n)!=n:
                #print("\nInvalid input. The input is not an integer.")
                error = True
            elif n<=1:
                #print("\nInvalid input. The input is <=1.")
                error = True
            """
        else:
            error = True

    
        if error:
            return render_template('chakravala-method.html', form=form, error=error, title='Chakravala', scroll='chakravala')
        else:
            
            if verbose:
                return render_template('chakravala-method.html', form=form, iteration=iteration, text=text, title='Chakravala', scroll='chakravala')
            else:
                return render_template('chakravala-method.html', form=form, text=text, title='Chakravala', scroll='chakravala')
    
    else:
        return render_template('chakravala-method.html', form=form, title='Chakravala', scroll='chakravala')

