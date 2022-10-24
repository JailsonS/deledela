from flask import Flask
from mvc_flask import FlaskMVC
# from flask_session import Session


app = Flask(__name__, template_folder='app/templates')

#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"

#Session(app)

FlaskMVC(app)