from flask import render_template, url_for, flash, redirect, request, Response, jsonify
from application import app, db, bcrypt
from application.models import User, Team, Player
from flask_login import login_user, current_user, logout_user ,login_required


@app.route('/register', methods= ['POST'])
def register():
    package = request.json
    pwd=package["password"]
    hashed_pwd = bcrypt.generate_password_hash(pwd).decode('utf-8')
    user = User (username= package["username"], email=package["email"], password= hashed_pwd)
    db.session.add(user)
    db.session.commit()
    app.logger.info(f"user: {user}")
    return Response(f"added New user: {user.username}", mimetype='text/plain')


@app.route('/login', methods= ['PUT'])
def login():
    package = request.json
    user = User.query.filter_by(username=package["username"]).first()
    user and bcrypt.check_password_hash(user.password, package["password"])
    return Response(f"logged user in", mimetype='text/plain')




@app.route('/team', methods= ['PUT'])
def new_team():
    package = request.json
    current_user = User.query.filter_by().first()
    team = Team(team_name = package["team_name"], owner= current_user)
    db.session.add(team)
    db.session.commit()
    return Response(f"new team: {team.team_name} from user {current_user.username}", mimetype='text/plain')



@app.route('/read/allteams', methods=["GET"])
def read_team():
    all_teams = Team.query.all()
    teams_dict = {"teams":[]}
    for team in all_teams:
        teams_dict["teams"].append(
            {
                "team_name": team.team_name,
                "username" : team.owner.username
            }
        )
    return jsonify(teams_dict)

@app.route('/user', methods=["GET"])
def user():
    all_users = User.query.all()
    users_dict = {"Users":[]}
    for user in all_users:
        users_dict["Users"].append(
            {
                "username" : User.username
            }
        )
    return jsonify(users_dict)


@app.route('/user/check', methods=["GET"])
def user_check():
    package = request.json
    name = package["username"]
    user = User.query.get(name)
    users_dict = {
                "username" : user.username
            }
    return jsonify(users_dict)
