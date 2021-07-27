from flask import render_template, Blueprint
from .forms import AryabhatanDecoder, AryabhatanEncoder
from .aryabhatan_decoder import decoder
from .aryabhatan_encoder import encoder
#import sqlite3

aryabhatan = Blueprint('aryabhatan', __name__, static_folder='static', template_folder='templates')

@aryabhatan.route('/aryabhatan-decoder', methods=['POST', 'GET'])
def Decoder():

    form = AryabhatanDecoder()

    if form.validate_on_submit():

        data = form.Input.data
        scheme = form.Encoding.data
        #verbose = form.Verbose.data
        value, Data = decoder(data, scheme)#, verbose)
        #print(value, Data, Syllables_Data)

        return render_template('aryabhatan-decoder.html', form=form, value=value, Data=Data, title='Aryabhatan Number System')

    else:
        return render_template('aryabhatan-decoder.html', form=form, title='Aryabhatan Number System')

@aryabhatan.route('/aryabhatan-encoder', methods=['POST', 'GET'])
def Encoder():

    form = AryabhatanEncoder()

    if form.validate_on_submit():

        data = int(form.Input.data)
        options = int(form.Options.data)

        text, result = encoder(data, options)
        return render_template('aryabhatan-encoder.html', form=form, text=text, result=result, title='Aryabhatan Number System')

    else:
        return render_template('aryabhatan-encoder.html', form=form, title='Aryabhatan Number System')

