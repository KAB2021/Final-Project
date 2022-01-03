from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import uuid


app = Flask(__name__)

app.config['SECRET_KEY'] = str(uuid.uuid4())

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

from application import routes