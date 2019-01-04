from flask import Flask
import api
from flask_login import login_required
from setting import CURRENT_SETTINGS, DefaultSettings
from extensions import session, login_manager, db
from flask import render_template
from flask import send_from_directory
import os
from models.data import Wendu, User, AddParametersGroup
import json
import dateutil.parser as date_parser
import subprocess


def create_bp(app):
    app.register_blueprint(api.watch.bp, url_prefix="/watch")
    app.register_blueprint(api.load.bp, url_prefix="/load")
    app.register_blueprint(api.login.bp, url_prefix="/login")
    app.register_blueprint(api.set.bp, url_prefix="/set")
    app.register_blueprint(api.analys.bp, url_prefix="/analys")


def init_extensions(app):
    db.init_app(app)
    #session.init_app(app)
    login_manager.init_app(app)


def init_login(app):
    pass


def start_frequency():
    path = os.path.join(CURRENT_SETTINGS.root_path, 'frequency_pro.py')
    com = 'python ' + path
    subprocess.Popen(com, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def check_setting_json():
    if not os.path.exists(CURRENT_SETTINGS.settings_path):
        f = open(CURRENT_SETTINGS.settings_path, 'w', encoding='utf-8')
        data = dict()
        grade = 'grade'
        for i in range(1, 9):
            grade = grade[:5] + str(i)
            data[grade] = 1000
        data['temp_ratio'] = 0
        data['hum_ratio'] = 0
        data['start_time'] = "08:00"
        data['end_time'] = "20:00"
        data['audio_size'] = 50
        data['now_frequency'] = 1000
        f.write(json.dumps(data))
        f.close()


def create_app(settings=None):
    if settings is None:
        settings = DefaultSettings()

    app = Flask(__name__)
    app.config.from_object(settings)
    create_bp(app)
    init_extensions(app)
    check_setting_json()
    start_frequency()

    return app


app = create_app(CURRENT_SETTINGS)


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

#db.create_all()


@app.route("/start")
@login_required
def start():
    return render_template('index.html')


@app.route("/templates/<file_name>")
def load_templates(file_name):
    return render_template(file_name)


@app.route("/templates_group/<file_name>")
def load_templates_group(file_name):
    groups = AddParametersGroup.query.all()
    # groups_name = []
    # for group in groups:
    #     groups_name.append(group.name)
    return render_template(file_name, groups=groups)


@app.route("/templates_settings/<file_name>")
def load_templates_settings(file_name):
    with open(CURRENT_SETTINGS.settings_path, encoding='utf-8') as f:
        settings = json.load(f)
    return render_template(file_name, settings=settings)


'''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
request.form.get("key", type=str, default=None) 获取表单数据

request.args.get("key") 获取get请求参数

request.values.get("key") 获取所有参数
'''

if __name__ == '__main__':
    app.run(host="0.0.0.0",  port=5001)

