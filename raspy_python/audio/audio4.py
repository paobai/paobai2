import math
#sudo apt-get install python-pyaudio
from pyaudio import PyAudio
import wave
import array

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.      

#See http://www.phy.mtu.edu/~suits/notefreqs.html
FREQUENCY = 1000 #Hz, waves per second, 261.63=C4-note.
LENGTH = 2 #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = []    

for x in range(NUMBEROFFRAMES):
   WAVEDATA.append(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))  

#fill remainder of frameset with silence
for x in range(RESTFRAMES): 
    WAVEDATA.append(128)
# b = array.array('B', WAVEDATA).tostring()
b = array.array('B', WAVEDATA).tostring()
p = PyAudio()
stream = p.open(
    format=p.get_format_from_width(1),
    channels=1,
    rate=BITRATE,
    output=True,
    )
stream.write(b)
stream.stop_stream()
stream.close()
p.terminate()


# wf = wave.open(r'C:\Users\Administrator\Desktop\毕设\论文下载\test1.wav', 'wb')
# wf.setnchannels(1)
# wf.setsampwidth(p.get_sample_size(1))
# wf.setframerate(16000)
# wf.writeframes(b)
# wf.close()
