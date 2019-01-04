#!/usr/bin/python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------#
#   Srit Software LTD Corporation Confidential                      #
#   All Rights Reserved.                                            #
#                                                                   #
#   NOTICE:  All information contained herein is, and remains       #
#   the property of  Srit Software LTD Corporation. The             #
#   intellectual and technical concepts contained herein are        #
#   proprietary to Srit Software LTD Corporation, and are           #
#   protected by trade secret or copyright law. Dissemination of    #
#   this information or reproduction of this material is strictly   #
#   forbidden unless prior written permission is obtained           #
#   Srit Software LTD Corporation.                                  #
#-------------------------------------------------------------------#
from flask import Blueprint, render_template, make_response
import json
from flask import g,request
from models.data import Wendu,Shidu
from models.data import *
from flask_login import login_required
import os
from setting import CURRENT_SETTINGS

bp = Blueprint("set", __name__)
settings_path = CURRENT_SETTINGS.settings_path


def generate_settings():
    with open(settings_path, encoding='utf-8') as f:
        return json.load(f)


def update_settings(new_settings):
    my_settings = generate_settings()
    with open(settings_path, 'w', encoding='utf-8') as f:
        for key, value in new_settings.items():
            if 'grade' in key:
                new_settings[key] = int(value)
            elif 'radio' in key:
                new_settings[key] = int(value)
            elif 'size' in key:
                new_settings[key] = int(value)
        my_settings.update(new_settings)
        f.write(json.dumps(my_settings))


@bp.route("/set_grade_frequency_form", methods=['GET', 'POST'])
def set_grade_frequency_form():
    new_settings = request.values.dicts[1].to_dict()
    update_settings(new_settings)
    return make_response('保存成功！'), 200


@bp.route("/set_other_parameters", methods=['GET', 'POST'])
def set_other_parameters():
    new_settings = request.values.dicts[1].to_dict()
    update_settings(new_settings)
    return make_response('保存成功！'), 200
