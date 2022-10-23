from flask import Flask
from mvc_flask import FlaskMVC


app = Flask(__name__, template_folder='app/templates')

FlaskMVC(app)