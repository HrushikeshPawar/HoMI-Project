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

        data = form.Input.data
        scheme = form.Encoding.data
        verbose = form.Verbose.data

        string, breakup, available = decoder(data, DATABASE, scheme)

        if not available:
            return render_template('bhutasankhya-decoder.html', form=form, error=True, title='Bhutasankhya', scroll='decoder')
        
        else:
            if verbose:
                return render_template('bhutasankhya-decoder.html', form=form, normal=string[::-1], reverse=string, breakup=breakup,  title='Bhutasankhya', scroll='decoder')
            else:
                return render_template('bhutasankhya-decoder.html', form=form, normal=string[::-1], reverse=string,  title='Bhutasankhya', scroll='decoder')

    else:
        return render_template('bhutasankhya-decoder.html', form=form, title='Bhutasankhya', scroll='decoder')

@bhutasankhya.route('/bhutasankhya-encoder', methods=['POST', 'GET'])
def Encoder():

    form = BhutasankhyaEncoder()
    
    if form.validate_on_submit():

        data = form.Input.data

        choices, available = encoder(data, DATABASE)

        if not available:
            return render_template('bhutasankhya-decoder.html', form=form, available=available, title='Bhutasankhya', scroll='encoder')
        
        else:
            return render_template('bhutasankhya-decoder.html', form=form, choices=choices,  title='Bhutasankhya', scroll='encoder')

    else:
        return render_template('bhutasankhya-decoder.html', form=form, title='Bhutasankhya', scroll='encoder')
