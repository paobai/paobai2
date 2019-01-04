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
import json
import math
from pyaudio import PyAudio
import wave
import array
from api.set import generate_settings, update_settings

Fs = 44000
T = 3
n = Fs*T
f = 1000

y = []
for x in range(n):
    y.append(int(math.sin(2 * math.pi * f / Fs * x) * 127 + 128))
b = array.array('B', y).tobytes()

for i in range(6):
    if i == 2:
        setting = dict(now_frequency=500)
        update_settings(setting)
    elif i == 4:
        setting = dict(now_frequency=1000)
        update_settings(setting)
    settings = generate_settings()
    if f != settings['now_frequency']:
        f = settings['now_frequency']
        print('change frequency!'+'-'+str(i) + '-'+str(f) + '-'+str(settings['now_frequency']))
        y = []
        for x in range(n):
            y.append(int(math.sin(2*math.pi*f/Fs*x)*127 + 128))
        b = array.array('B', y).tobytes()

    p = PyAudio()
    stream = p.open(
        format=p.get_format_from_width(1),
        channels=1,
        rate=44000,
        output=True,
        )
    stream.write(b)
    stream.stop_stream()
    stream.close()
    p.terminate()
