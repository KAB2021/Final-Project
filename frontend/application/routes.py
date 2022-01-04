from flask import render_template, url_for, flash, redirect
from application import app, db, bcrypt
from application.form import RegistrationForm, LoginForm, NewTeamForm
from application.models import User, Team, Player
from flask_login import login_user, current_user, logout_user ,login_required

@app.route('/')
def home():
    teams= Team.query.all()
    return render_template("home.html", title="Home", teams=teams )

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
        flash(f'Account Created!', 'success')
        return redirect(url_for('login'))
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
    flash ('Logged out', 'success')
    return redirect(url_for('home'))

@app.route('/team', methods= ['GET', 'POST'])
@login_required
def new_team():
    form = NewTeamForm()
    if form.validate_on_submit():
        team = Team(team_name = form.team_name.data, owner= current_user)
        db.session.add(team)
        db.session.commit()
        flash(" Your team has been created", 'success' )
        return redirect(url_for('home'))
    return render_template("create_team.html", title="New Team", form = form)


