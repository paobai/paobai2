from flask import Blueprint,render_template, jsonify
import json
from flask import g,request
from models.data import Wendu,Shidu
from models.data import *
from flask_login import login_required
from setting import CURRENT_SETTINGS
from api.set import generate_settings
bp = Blueprint("watch", __name__)


@bp.route("/")
@login_required
def watch_the_state():
    return render_template('watch.html')


def generate_select_resutl(select_value,wendu_or_shidu):
    if wendu_or_shidu.lower() == "wendu":
        wendu_or_shidu=Wendu
    else:
        wendu_or_shidu=Shidu
    if select_value == '10minute':
        result = wendu_or_shidu.query.filter_by(time_style='10minute').order_by(wendu_or_shidu.save_time.desc()).limit(10).all()
    elif select_value == 'hour':
        result = wendu_or_shidu.query.filter_by(time_style='hour').order_by(wendu_or_shidu.save_time.desc()).limit(10).all()
    elif select_value == 'day':
        result = wendu_or_shidu.query.filter_by(time_style='day').order_by(wendu_or_shidu.save_time.desc()).limit(10).all()
    elif select_value == 'month':
        result = wendu_or_shidu.query.filter_by(time_style='month').order_by(wendu_or_shidu.save_time.desc()).limit(10).all()
    else:
        raise ValueError("错误参数")
    

    final_result = dict()
    time_list = []
    data_list = []
    for row in result:
        if select_value == '10minute':
            time_list.append(row.save_time.minute)
        elif select_value == 'hour':
            time_list.append(row.save_time.hour)
        elif select_value == 'day':
            time_list.append(row.save_time.day)
        elif select_value == 'month':
            time_list.append(row.save_time.month)
    
        data_list.append(float(row.data))
    final_result['time_list'] = time_list
    final_result['data_list'] = data_list
    final_result['count'] = len(data_list)
    return final_result


@bp.route("/wendu/24hour")
@login_required
def get_24_hour_wendu():
    select_value = request.values.get("value")
    final_result = generate_select_resutl(select_value, 'Wendu')
    return jsonify(final_result)


@bp.route("/shidu/24hour")
@login_required
def get_24_hour_shidu():
    select_value = request.values.get("value")
    final_result = generate_select_resutl(select_value, 'Shidu')
    return jsonify(final_result)


@bp.route("/state_now")
@login_required
def get_state_now():
    state = dict()
    wendu = Wendu.query.order_by(Wendu.save_time.desc()).first()
    shidu = Shidu.query.order_by(Shidu.save_time.desc()).first()
    state['wendu'] = wendu.data
    state['shidu'] = shidu.data

    seggitngs = generate_settings()
    state['frequency'] = seggitngs['now_frequency']
    state['size'] = seggitngs['audio_size']

    return json.dumps(state)


@bp.route("/state_all")
@login_required
def get_state_html():

    return render_template('watch_text.html')
