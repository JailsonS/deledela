
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from app.forms import LoginForm

from app.models.User import User

class AuthController:

    def login(self):
        return render_template("auth/login.html", form=LoginForm())

    def do_login(self):
        
        form = LoginForm()
        
        # validate form data
        if not form.validate_on_submit():
            print(1)
            return render_template("auth/login.html", form=LoginForm())    
        
        # validate user
        user = User

        user.name = 'User'
        user.email = form.email.data
        user.password = form.password.data

        return redirect('home')  
