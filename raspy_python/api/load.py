from flask import Blueprint, render_template, make_response
import os
from flask import render_template,request,render_template, send_from_directory, request, jsonify
import json
from setting import CURRENT_SETTINGS
import datetime
import time
from extensions import db
from models.data import Wendu, Shidu, AddParametersData, AddParametersGroup
from flask import g


bp = Blueprint("load", __name__)
basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前项目的绝对路径
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF','py'])  # 允许上传的文件后缀


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@bp.route('/123',methods = ['POST','GET'])
def hello_world():
    if request.method == "POST":
        return (json.dumps(request.form))
    a=dict()
    b=[1,2,3]
    a['11']=b
    a['22']=321
    return json.dumps(a)

@bp.route('/')
def upload_test():
    return render_template('upload.html')


@bp.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(CURRENT_SETTINGS.root_path, CURRENT_SETTINGS.UPLOAD_FOLDER)  # 拼接成合法文件夹地址
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)  # 文件夹不存在就创建
    f=request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值
    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
        fname=f.filename
        ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
        unix_time = int(time.time())
        #new_filename = str(unix_time)+'.'+ext   # 修改文件名
        fname_dir = os.path.join(file_dir, fname)
        while(os.path.exists(fname_dir)):
            fname = fname.rsplit('.', 1)[0] + '1.' +fname.rsplit('.', 1)[1]
            fname_dir = os.path.join(file_dir, fname)
        f.save(os.path.join(file_dir, fname))  #保存文件到upload目录

        return jsonify({"errno": 0, "errmsg": "上传成功"})
    else:
        return jsonify({"errno": 1001, "errmsg": "上传失败"})


@bp.route("/download/<path:filename>")
def downloader(filename):
    username = request.values.get("analys_select")
    dirpath = os.path.join(CURRENT_SETTINGS.root_path, 'upload')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载


@bp.route("/save_state", methods=['POST'])
def save_state():
    now_wendu = request.form['wendu']
    now_shidu = request.form['shidu']
    now = datetime.datetime.now()
    style_list = generate_time_style_list(now)

    for time_style in style_list:

        wendu = Wendu(data=now_wendu,save_time=now,time_style=time_style)
        shidu = Shidu(data=now_shidu,save_time=now,time_style=time_style)
        db.session.add(wendu)
        db.session.add(shidu)
        db.session.commit()
    return 'ok'


@bp.route("/create", methods=['GET'])
def create_special():
    return render_template('index.html')


@bp.route("/load_create_form", methods=['GET', 'POST'])
def load_create_form():
    name = request.values['name']
    description = request.values['description']
    unit = request.values['unit']
    if AddParametersGroup.query.filter_by(name=name).first():
        return make_response('名字重复,请重选或者在已有基础上记录。'), 500
    group = AddParametersGroup(name=name, description=description, unit=unit)
    db.session.add(group)
    db.session.commit()
    return make_response('成功创建！'), 200


@bp.route("/load_save_form", methods=['GET', 'POST'])
def load_save_form():
    id = request.values['load_select']
    value = request.values['value']
    group = AddParametersGroup.query.get(id)
    data = AddParametersData(name=group.name, value=value, group_id=group.id, save_time=datetime.datetime.now())
    db.session.add(data)
    db.session.commit()
    return make_response('成功储存'), 200


def generate_time_style_list(now_time):
    style_list = ['10minute']
    if now_time.minute >=29 and now_time.minute<=31:
        style_list.append('hour')
    if now_time.hour == 12 and now_time.minute >=29 and now_time.minute<=31:
        style_list.append('day')
    if now_time.day == 15 and now_time.hour == 12 and now_time.minute >=29 and now_time.minute<=31:
        style_list.append('month')
    return style_list

