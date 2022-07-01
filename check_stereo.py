import json, wave, contextlib
import os

sourcePath = os.path.join(os.getcwd(), 'datasets/sorted/TORGO')

for each_file in os.listdir(sourcePath):
    with contextlib.closing(wave.open(each_file,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        print(f.getnchannels)
        #duration = frames / float(rate)
        #print("Duration in seconds is: " + str(duration))
        #return duration