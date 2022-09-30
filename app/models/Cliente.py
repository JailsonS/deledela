from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente:
    __tablename__ = 'PCCLIENT'

    codcli = db.Column(db.VARCHAR2(50))
    cliente = db.Column(db.VARCHAR2(50))