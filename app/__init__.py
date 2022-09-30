from flask import Flask
from mvc_flask import FlaskMVC


app = Flask(__name__)


FlaskMVC(app)