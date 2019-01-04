from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
session = Session()
login_manager = LoginManager()
login_manager.login_view = 'login.loginhtml'

#loginManager.session_protection="strong"
#loginManager.login_view="login"