from flask import Flask, render_template, g
from flaskext.markdown import Markdown
from .Sexagesimal.sexagesimalCalculator import sexagesimal
from .Katapayadi.katapayadi import katapayadi
from .Aryabhatan.aryabhatan_system import aryabhatan
import sqlite3

app = Flask(__name__, static_url_path='/static')
app.register_blueprint(sexagesimal, url_prefix='/tools')
app.register_blueprint(aryabhatan, url_prefix='/tools')
app.register_blueprint(katapayadi, url_prefix='/tools')

app.config['SECRET_KEY'] = 'a54d04a4ce38193acc5407a681df2400'

Markdown(app)
DATABASE = 'Demo_Database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db == None:
        db = g._database = sqlite3.connect(DATABASE)
    
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/home')
@app.route('/')
def main():
    return render_template('home.html')

@app.route('/katapayadi')
def katapayadi_system():
    return render_template('katapayadi.html')

@app.route('/sexagesimal')
def sexagesimal_system():
    return render_template('sexagesimal.html')

@app.route('/aryabhatan')
def aryabhatan_system():
    return render_template('aryabhatan.html')




if __name__ == '__main__':
    app.run(debug=True)