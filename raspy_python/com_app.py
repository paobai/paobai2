from creatapp import create_app
from setting import CURRENT_SETTINGS
from flask_script import Command, Shell, Manager
from models.data import *
from extensions import db
app = create_app(CURRENT_SETTINGS)
app.app_context().push()

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()