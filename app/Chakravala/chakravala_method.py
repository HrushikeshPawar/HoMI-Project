from flask import Blueprint, render_template
from .forms import ChakravalaForm
from .Chakravala import chakravala, chakravala_with_Bhramhaguptas_shortcut, LagrangeMethod
from math import sqrt

Chakravala = Blueprint('Chakravala', __name__, static_folder='static', template_folder='templates')

@Chakravala.route('/chakravala-calculator', methods=['POST', 'GET'])
def chakravala_method():

    form = ChakravalaForm()

    if form.validate_on_submit():

        n = form.Input.data
        algorithm = form.Algorithm.data
        verbose = form.Verbose.data

        try:
            if n>1 and int(sqrt(n))!=sqrt(n) and int(n)==n:

                if algorithm == '''Lagrange's Method to solve Pell's Equation''':
                    iteration = LagrangeMethod(n)
                    text = f'''\n We are using Lagrange's method of continued fractions to solve a<sup>2</sup> = {n}b<sup>2</sup> + 1.
                    
                    \nFor n = {n}, we need {len(iteration)} iterations to arrive at an answer.

                    \nThe smallest integer solution for a<sup>2</sup> = {n}b<sup>2</sup> + 1 
                    
                    a = {iteration[-1][0]} and b = {iteration[-1][1]}
                    '''
                
                elif algorithm == '''Chakravala with Bhramhaguta's Shortcuts''':
                    iteration = chakravala_with_Bhramhaguptas_shortcut(n)
                    text = f'''\n We are using chakravala with Bhramhaguta's shortcuts to solve a<sup>2</sup> = {n}b<sup>2</sup> + 1.
                
                    \n Begin with the general equation a<sup>2</sup> = {n}b<sup>2</sup> + m and apply chakravala till m equals 1 (when the program ends) or m equals -1, 2, -2, 4 or -4 (when we apply shortcuts).
                    
                    \nFor n = {n}, we need {len(iteration)} iterations to arrive at an answer.

                    \nThe smallest integer solution for a<sup>2</sup> = {n}b<sup>2</sup> + 1 
                    
                    a = {iteration[-1][0]} and b = {iteration[-1][1]}
                    '''
                
                else:
                    iteration = chakravala(n)
                    text = f'''\n We are using chakravala to solve a<sup>2</sup> = {n}b<sup>2</sup> + 1.
                
                    \n Begin with the general equation a<sup>2</sup> = {n}b<sup>2</sup> + m and apply chakravala till m equals 1.
                    
                    \nFor n = {n}, we need {len(iteration)} iterations to arrive at an answer.

                    \nThe smallest integer solution for a<sup>2</sup> = {n}b<sup>2</sup> + 1 
                    
                    a = {iteration[-1][0]} and b = {iteration[-1][1]}
                    '''
                    
                error = False
            else:
                error = True
        
        except Exception as e:
            print(e)
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

