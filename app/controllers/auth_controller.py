
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.forms import LoginForm

from app.models.User import User

class AuthController:

    def login(self):
        return render_template("auth/login.html", form=LoginForm())

    def do_login(self):
        
        form = LoginForm()

        data = request.form


        if form.validate_on_submit() is False:
            return render_template("auth/login.html", form=LoginForm())    
        
        user = User('Usuário', form.email.data, form.password.data)
