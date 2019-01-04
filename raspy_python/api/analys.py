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
from flask import Blueprint,render_template, send_file, jsonify
import json
from flask import g,request
from models.data import *
from flask_login import login_required
import xlwt.CompoundDoc
import xlwt
import io

bp = Blueprint("analys", __name__)


@bp.route("/analys_export", methods=['GET', 'POST'])
def analys_export():
    group_id = request.values['analys_select']
    start_time = request.values['start_time']
    end_time = request.values['end_time']
    group = AddParametersGroup.query.get(group_id)
    q = AddParametersData.query.filter(AddParametersData.group_id == group_id)
    q = q.filter(AddParametersData.save_time > start_time)
    res = q.filter(AddParametersData.save_time < end_time).all()

    writebook = xlwt.Workbook()
    sheet = writebook.add_sheet('result')  # 在打开的excel中添加一个sheet
    sheet.write(0, 0, '补充参数名' + group.name)
    sheet.write(1, 0, group.name)
    sheet.write(0, 1, '补充参数单位' + group.unit)
    sheet.write(1, 1, group.unit)
    sheet.write(0, 2, '补充参数备注' + group.description)
    sheet.write(1, 2, group.description)

    sheet.write(2, 0, '补充参数的值')
    sheet.write(2, 1, '补充参数的记录时间')
    line = 3
    for col in res:
        sheet.write(line, 0, col.value)
        sheet.write(line, 1, str(col.save_time))
        line += 1

    stream = io.BytesIO()
    writebook.save(stream)
    stream.seek(0)
    resp = send_file(stream, mimetype='text/csv', as_attachment=True, attachment_filename='down_load.xls')
    return resp, 200


@bp.route("/analys_generate_line", methods=['GET', 'POST'])
def analys_generate_line():
    group_id = request.values['analys_select']
    start_time = request.values['start_time']
    end_time = request.values['end_time']
    group = AddParametersGroup.query.get(group_id)
    q = AddParametersData.query.filter(AddParametersData.group_id == group_id)
    q = q.filter(AddParametersData.save_time > start_time)
    res = q.filter(AddParametersData.save_time < end_time).all()

    final_dict = dict()
    title = group.name
    data_list = []
    time_list = []
    for col in res:
        data_list.append(col.value)
        time_list.append(str(col.save_time))
    final_dict['data_list'] = data_list
    final_dict['time_list'] = time_list
    final_dict['title'] = title + '的记录情况'
    final_dict['count'] = len(data_list)
    return jsonify(final_dict), 200
