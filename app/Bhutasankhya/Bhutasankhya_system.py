from .Bhtasankhya_Encoder_Decoder import encoder, decoder
from .forms import BhutasankhyaDecoder, BhutasankhyaEncoder
import os
from flask import Blueprint, render_template

bhutasankhya = Blueprint('bhutasankhya', __name__, static_folder='static', template_folder='templates')

# Database path
#DATABASE = os.path.join('static', 'data', 'data.json')
DATABASE = 'data.json'

@bhutasankhya.route('/bhutasankhya-decoder', methods=['POST', 'GET'])
def Decoder():

    form = BhutasankhyaDecoder()

    if form.validate_on_submit():

        data = form.Input.data.strip()
        scheme = form.Encoding.data
        verbose = form.Verbose.data

        string, breakup, available, Input = decoder(data, DATABASE, scheme)
        normal = "".join(string)
        reverse = "".join(string[::-1])

        if available == 'Invalid Input':
            invalid = 'Invalid Input. Please check if right scheme is selected and there are no spelling mistakes.'
            return render_template('bhutasankhya-decoder.html', form=form, invalid=invalid, title='Bhutasankhya', scroll='decoder')

        

        if not available:
            return render_template('bhutasankhya-decoder.html', form=form, error=True, title='Bhutasankhya', scroll='decoder')
        
        else:
            if verbose:
                return render_template('bhutasankhya-decoder.html', form=form, Input=Input, normal=normal, reverse=reverse, breakup=breakup,  title='Bhutasankhya', scroll='decoder')
            else:
                return render_template('bhutasankhya-decoder.html', form=form, Input=Input, normal=normal, reverse=reverse,  title='Bhutasankhya', scroll='decoder')

    else:
        return render_template('bhutasankhya-decoder.html', form=form, title='Bhutasankhya', scroll='decoder')

@bhutasankhya.route('/bhutasankhya-encoder', methods=['POST', 'GET'])
def Encoder():

    form = BhutasankhyaEncoder()
    
    if form.validate_on_submit():

        n = str(form.Input.data)
        k = form.Options.data

        Normal, Reverse  = encoder(n, k, DATABASE)
        
        if Normal[-1] != False:
            normal_choices = Normal[0]
            normal_flag = Normal[-1]
            normal_breakup = []
        else:
            normal_choices = Normal[0]
            normal_breakup = Normal[1]
            normal_flag = []
        
        if Reverse[-1] != False:
            reverse_choices = Reverse[0]
            reverse_flag = Reverse[-1]
            reverse_breakup = []
        else:
            reverse_choices = Reverse[0]
            reverse_breakup = Reverse[1]
            reverse_flag = []
        

        if normal_breakup == [] and reverse_breakup == []:
            return render_template('bhutasankhya-encoder.html', form=form, normal_choices=normal_choices, reverse_choices=reverse_choices, normal_flag=normal_flag, reverse_flag=reverse_flag, k=k, title='Bhutasankhya', scroll='encoder')
        
        elif normal_breakup == [] and reverse_breakup != []:
            return render_template('bhutasankhya-encoder.html', form=form, normal_choices=normal_choices, reverse_choices=reverse_choices, normal_flag=normal_flag, reverse_breakup=reverse_breakup, k=k, title='Bhutasankhya', scroll='encoder')
        
        elif normal_breakup != [] and reverse_breakup == []:
            return render_template('bhutasankhya-encoder.html', form=form, normal_choices=normal_choices, reverse_choices=reverse_choices, normal_breakup=normal_breakup, reverse_flag=reverse_flag, k=k, title='Bhutasankhya', scroll='encoder')
        
        elif normal_breakup != [] and reverse_breakup != []:
            return render_template('bhutasankhya-encoder.html', form=form, normal_choices=normal_choices, reverse_choices=reverse_choices, normal_breakup=normal_breakup, reverse_breakup=reverse_breakup, k=k, title='Bhutasankhya', scroll='encoder')
        
        else:
            print('Error')
        

        """
        if breakup != 'non-split':
            return render_template('bhutasankhya-encoder.html', form=form, choices=choices, breakup=breakup, Encodings=Encodings
                                    , title='Bhutasankhya', scroll='encoder')
        
        else:

            if flag > k:
                text = f'The database has {flag} different options for number {n}. Showing {k} random options.'
                return render_template('bhutasankhya-encoder.html', form=form, text=text, choices=choices,  title='Bhutasankhya', scroll='encoder')
            
            elif flag < k:
                text = f'The database has only {flag} different options for number {n}. Showing all available options.'
                return render_template('bhutasankhya-encoder.html', form=form, text=text, choices=choices,  title='Bhutasankhya', scroll='encoder')
            
            else:
                text = f'The database has exactly {flag} different options for number {n}. Showing all available options.'
                return render_template('bhutasankhya-encoder.html', form=form, text=text, choices=choices,  title='Bhutasankhya', scroll='encoder')
        """
    else:
        return render_template('bhutasankhya-encoder.html', form=form, title='Bhutasankhya', scroll='encoder')
