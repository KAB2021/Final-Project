from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    teams = db.relationship('Team', backref= 'owner', lazy=True)

    def __repr__(self):
        return f"user('{self.username}')"


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Team('{self.team_name}')"

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"Player ('{self.player}')"




    






    







