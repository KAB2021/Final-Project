from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import getenv


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")



db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

from application import routes