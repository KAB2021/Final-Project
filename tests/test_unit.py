from flask_testing import TestCase
from application import app, db, bcrypt
from application.models import User, Team
from flask import url_for, session, request


class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        user = User(username='admin', email='admin@admin.com',
                    password='password')
        db.session.add(user)
        db.session.commit()

        team = Team(team_name='red', user_id=user.id)
        db.session.add(team)
        db.session.commit()

    def set_session_cookie(client):
        val = app.session_interface.get_signing_serializer(
            app).dumps(dict(session))
        client.set_cookie('localhost', app.session_cookie_name, val)

    def tearDown(self):
        db.drop_all()


class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assert200(response)

    def test_about_get(self):
        response = self.client.get(url_for("about"))
        self.assert200(response)

    def test_login_get(self):
        response = self.client.get(url_for("login"))
        self.assert200(response)

    def test_register_get(self):
        response = self.client.get(url_for("register"))
        self.assert200(response)

class TestViews1(TestBase):
    def test_logout_get(self):
        app.config['LOGIN_DISABLED'] = True
        response = self.client.get(url_for("logout"))
        follow_redirects = True
        self.assertEqual(response.status_code, 302)


class TestRead(TestBase):
    def test_read_tasks(self):
        response = self.client.get(url_for("home"))
        self.assertIn("home", str(response.data))

    def test_read_tasks(self):
        response = self.client.get(url_for("about"))
        self.assertIn("about", str(response.data))


# class TestCreate2(TestBase):
#     def test_login_user(self):
#         response = self.client.post(
#             url_for("login"),
#             json={"username": "admin", "password": "password"},
#             follow_redirects=True)
#         self.assertEqual(response.status_code, 302)


class TestCreate(TestBase):
    
    def test_create_user(self):
        response = self.client.post(
            url_for("register"),
            json={"username": "admin1", "email": "admin1@admin.com",
                  "password": "password","confirm_password": "password" },
            follow_redirects=True)
        new_user = User.query.get(2)
        self.assertEqual("admin1", new_user.username)    
    
class TestCreate1(TestBase):
    
    def test_create_team(self):
        @app.login_manager.request_loader
        def load_user_from_request(request):
            return User.query.first()
        response = self.client.post(
            url_for("new_team"),
            json={"team_name": "blue"},
            follow_redirects=True)
        new_team = Team.query.get(2)
        self.assertEqual("blue", new_team.team_name)


