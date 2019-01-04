import mmap
import math
import pyaudio,wave
import array


# fh = open('K:\out.txt', 'rb')

# m = mmap.mmap(fh.fileno(), 0, access=mmap.ACCESS_READ)
# ba = bytearray(m)

#ba = [300,400,500,400,200]
#sudo apt-get install python-pyaudio
PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),
               channels = 1,
               rate = BITRATE,
               output = True)

wf=wave.open(r'C:\Users\Administrator\Desktop\毕设\论文下载\test3.wav',"wb")
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(pyaudio.paInt8))  # byte = 8 bits else trashed
wf.setframerate(BITRATE)


# for freq in ba:
# #See http://www.phy.mtu.edu/~suits/notefreqs.html
#    FREQUENCY = 300 + freq #Hz, waves per second, 261.63=C4-note.
#    print('freq '+str(FREQUENCY))
#    LENGTH = 1 #seconds to play sound

#    NUMBEROFFRAMES = int(BITRATE * LENGTH)
#    RESTFRAMES = NUMBEROFFRAMES % BITRATE
#    WAVEDATA = list()


#    for x in range(NUMBEROFFRAMES):
#     v = int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128)
#     WAVEDATA.append(v)

#    #fill remainder of frameset with silence
#    WAVEDATA+=[128]*RESTFRAMES

#    b = array.array('B', WAVEDATA).tostring()

#    wf.writeframes(b)
#    stream.write(b)




FREQUENCY = 300 + 1000 #Hz, waves per second, 261.63=C4-note.
print('freq '+str(FREQUENCY))
LENGTH = 3 #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = list()


for x in range(NUMBEROFFRAMES):
    v = int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128)
    WAVEDATA.append(v)

#fill remainder of frameset with silence
WAVEDATA+=[128]*RESTFRAMES

b = array.array('B', WAVEDATA).tostring()

wf.writeframes(b)
stream.write(b)

#print data
wf.close()
stream.stop_stream()
stream.close()
p.terminate()