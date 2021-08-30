from flask import Blueprint, render_template
from .forms import CakravalaForm
from .Cakravala import cakravala, Cakravala_with_Bhramhaguptas_shortcut, LagrangeMethod
from math import sqrt

Cakravala = Blueprint('cakravala', __name__, static_folder='static', template_folder='templates')

@Cakravala.route('/cakravala-calculator', methods=['POST', 'GET'])
def Cakravala_method():

    form = CakravalaForm()

    if form.validate_on_submit():

        n = form.Input.data
        algorithm = form.Algorithm.data
        verbose = form.Verbose.data

        try:
            if n>1 and int(sqrt(n))!=sqrt(n) and int(n)==n:

                if algorithm == '''Lagrange's Method to solve Pell's Equation''':
                    iteration = LagrangeMethod(n)
                    if len(iteration) == 1:
                        iter = 'iteration'
                    else:
                        iter = 'iterations'
                    text = f'''\n We are using **Lagrange's method of continued fractions** to solve a<sup>2</sup> = {n}b<sup>2</sup> + 1.
                    
                    \nFor n = {n}, we need **{len(iteration)} {iter}** to arrive at an answer.

                    \nThe smallest integer solution for a<sup>2</sup> = {n}b<sup>2</sup> + 1 is **a = {iteration[-1][0]} and b = {iteration[-1][1]}**
                    '''
                
                elif  '''Bhramhaguta's Shortcuts''' in algorithm :
                    iteration = Cakravala_with_Bhramhaguptas_shortcut(n)
                    if len(iteration) == 1:
                        iter = 'iteration'
                    else:
                        iter = 'iterations'
                    text = f'''\n We are using **Cakravala with Bhramhaguta's shortcuts** to solve a<sup>2</sup> = {n}b<sup>2</sup> + 1.
                
                    \n Begin with the general equation a<sup>2</sup> = {n}b<sup>2</sup> + m and apply cakravala till m equals 1 (when the program ends) or m equals -1, 2, -2, 4 or -4 (when we apply shortcuts).
                    
                    \nFor n = {n}, we need **{len(iteration)} {iter}** to arrive at an answer.

                    \nThe smallest integer solution for a<sup>2</sup> = {n}b<sup>2</sup> + 1 is **a = {iteration[-1][0]} and b = {iteration[-1][1]}**
                    '''
                
                else:
                    iteration = cakravala(n)
                    if len(iteration) == 1:
                        iter = 'iteration'
                    else:
                        iter = 'iterations'
                    text = f'''\n We are using **Cakravala** to solve a<sup>2</sup> = {n}b<sup>2</sup> + 1.
                
                    \n Begin with the general equation a<sup>2</sup> = {n}b<sup>2</sup> + m and apply cakravala till m equals 1.
                    
                    \nFor n = {n}, we need **{len(iteration)} {iter}** to arrive at an answer.

                    \nThe smallest integer solution for a<sup>2</sup> = {n}b<sup>2</sup> + 1 is **a = {iteration[-1][0]} and b = {iteration[-1][1]}**
                    '''
                    
                error = False
            else:
                error = True
        
        except Exception as e:
            print(e)
            error = True

    
        if error:
            return render_template('cakravala-method.html', form=form, error=error, title='cakravala', scroll='cakravala')
        else:
            
            if verbose:
                return render_template('cakravala-method.html', form=form, iteration=iteration, text=text, title='cakravala', scroll='cakravala')
            else:
                return render_template('cakravala-method.html', form=form, text=text, title='cakravala', scroll='cakravala')
    
    else:
        return render_template('cakravala-method.html', form=form, title='cakravala', scroll='cakravala')

