from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
import logging


import cx_Oracle
import os

load_dotenv()

engine = create_engine('oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{sid}'.format(
  username=os.getenv('DB_USER'),
  password=os.getenv('DB_PASS'),
  hostname=os.getenv('DB_HOSTNAME'),
  port=os.getenv('DB_PORT'),
  sid=os.getenv('DB_NAME'),
), implicit_returning=False)


logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)