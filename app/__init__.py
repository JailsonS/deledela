from flask import Flask
from mvc_flask import FlaskMVC
from flask_session import Session


app = Flask(__name__, template_folder='app/templates')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = '12345'

Session(app)

FlaskMVC(app)