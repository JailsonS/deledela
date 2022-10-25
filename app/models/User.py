from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):

    def __init__(self, name, email, password) -> None:
        super().__init__()

        self.name = name
        self.email = email
        self.password = password
        self.pwd_hash = ''

    @property
    def password(self):
        return AttributeError("cannot read password")

    @password.setter
    def password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def valid_password(self, password):
        return check_password_hash(self.pwd_hash, password)

    @property
    def name(self):
        return self.name

    @property
    def email(self):
        return self.email