from flask import render_template, Blueprint, g
from .forms import KatapayadiDecoder, KatapayadiEncoder
from .katapayadi_decoder import decoder
from .katapayadi_encoder import Katapayadi_Encoder
import sqlite3

katapayadi = Blueprint('katapayadi', __name__, static_folder='static', template_folder='templates')
DATABASE = 'Demo_Database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db == None:
        db = g._database = sqlite3.connect(DATABASE)  
    return db

@katapayadi.route('/katapayadi-decoder', methods=['POST', 'GET'])
def Decoder():

    form = KatapayadiDecoder()

    if form.validate_on_submit():

        data = form.Input.data
        scheme = form.Encoding.data
        verbose = form.Verbose.data
        Decoded_Values, Verbose_Data = decoder(data, scheme, verbose)
        normal_value, reverse_value = Decoded_Values
        Data, Syllables_Data = Verbose_Data

        if verbose:
            return render_template('katapayadi-decoder.html', form=form, normal=normal_value, reverse=reverse_value, Data=Data, Syllables_Data=Syllables_Data)
        else:
            return render_template('katapayadi-decoder.html', form=form, normal=normal_value, reverse=reverse_value)
    else:
        return render_template('katapayadi-decoder.html', form=form)

@katapayadi.route('/katapayadi-encoder', methods=['POST', 'GET'])
def Encoder():

    form = KatapayadiEncoder()

    if form.validate_on_submit():

        data = str(form.Input.data)
        options = str(form.Options.data)
        Database = get_db()

        N_Words_lable, N_Words, R_Words_lable, R_Words, N_Sentences_Dict, R_Sentences_Dict = Katapayadi_Encoder(data, options, Database)
        N_Sentences_Dict_Keys, N_Sentences_Dict_Values = list(N_Sentences_Dict.keys()), list(N_Sentences_Dict.values())
        R_Sentences_Dict_Keys, R_Sentences_Dict_Values = list(R_Sentences_Dict.keys()), list(R_Sentences_Dict.values())
        return render_template('katapayadi-encoder.html', form=form, N_Words_lable=N_Words_lable, N_Words=N_Words, R_Words=R_Words
                                , R_Words_lable=R_Words_lable, N_Sentences_Dict_Keys=N_Sentences_Dict_Keys
                                , N_Sentences_Dict_Values=N_Sentences_Dict_Values, R_Sentences_Dict_Keys=R_Sentences_Dict_Keys
                                , R_Sentences_Dict_Values=R_Sentences_Dict_Values)

    else:
        return render_template('katapayadi-encoder.html', form=form)