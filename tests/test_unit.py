from flask_testing import TestCase
from application import app, db, bcrypt
from application.models import User, Team
from flask import url_for


class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI ="sqlite:///",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()

        user = User(username ='admin',email ='admin@admin.com', password='password' )
        db.session.add(user)
        db.session.commit()
        
        team = Team(team_name='red', user_id = user.id)
        db.session.add(team)
        db.session.commit()



    def tearDown(self):
        # Will be called after every test
        db.drop_all()


class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)

    def test_about_get(self):
        response = self.client.get(url_for("about"))
        self.assert200(response)

    def test_register_get(self):
        response = self.client.get(url_for("register"))
        self.assert200(response)
    
    def test_login_get(self):
        response = self.client.get(url_for("login"))
        self.assert200(response)
    
    





