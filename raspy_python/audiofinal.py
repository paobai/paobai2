import math
#sudo apt-get install python-pyaudio
from pyaudio import PyAudio
import pyaudio
import wave
import array

Fs = 44000
T = 3
n = Fs*T
f = 1000
y = []
for x in range(n):

    y.append(int(math.sin(2*math.pi*f/Fs*x)*127 + 128 ))

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

# wf = wave.open(r'C:\Users\Administrator\Desktop\毕设\论文下载\test5.wav', 'wb')
# wf.setnchannels(1)
# wf.setsampwidth(p.get_sample_size(pyaudio.paInt8))
# wf.setframerate(16000)
# wf.writeframes(b)
# wf.close()