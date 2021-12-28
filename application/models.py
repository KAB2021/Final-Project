from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    teams = db.relationship('Team', backref= 'owner', lazy=True)

    def __repr__(self):
        return f"user('{self.username}', '{self.email}', '{self.image_file}')"


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Team('{self.team_name}')"

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(20), nullable=False)
    player = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"Player ('{self.player}','{self.position}')"

class TeamPlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    player = db.relationship('Player', foreign_keys=[player_id], lazy=True)

    def __repr__(self):
        return f"Player ('{self.team_id}','{self.player_id}')"



    






    







