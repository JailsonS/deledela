from flask import Flask
from mvc_flask import FlaskMVC

from dotenv import load_dotenv

import cx_Oracle
import os

load_dotenv()

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@' + cx_Oracle.makedsn('{hostname}', '{port}', '{sid}')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = oracle_connection_string.format(
  username=os.getenv('DB_USER'),
  password=os.getenv('DB_PASS'),
  hostname=os.getenv('DB_HOSTNAME'),
  port=os.getenv('DB_PORT'),
  sid=os.getenv('DB_NAME'),
)

FlaskMVC(app)