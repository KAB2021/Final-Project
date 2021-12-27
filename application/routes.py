from flask import render_template, url_for, flash, redirect
from application import app, db, bcrypt
from application.form import RegistrationForm, LoginForm
from application.models import User
from flask_login import login_user, current_user, logout_user


@app.route('/')
def home():
    return render_template("home.html", title="Home", )

@app.route('/about')
def about():
    return render_template("about.html", title="about", )

@app.route('/register', methods= ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User (username= form.username.data, email=form.email.data, password= hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register",form=form )

@app.route('/login', methods= ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash ('Please check username and password', 'danger')
    return render_template("login.html", title="Login",form=form )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
