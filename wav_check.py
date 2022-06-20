import os
import wave
import contextlib

wav_loads = "UASpeech_F02_B1_C10_M4.wav"
#wav_loads2 = "UASpeech_F02_B1_C10_M4"
wav_error = "M14_B3_CW100_M3.wav"
#wav_error2 = "M14_B3_CW100_M3"

def get_properties(wav_path):
    with contextlib.closing(wave.open(wav_path,'r')) as f:
        for item in f.getparams():
            print(item)
        '''
        wav_nframes = f.getnframes()
        wav_framerate = f.getframerate()
        wav_comptype = f.getcomptype()
        wav_nchannels = f.getnchannels()
        wav_compname = f.getcompname()
        wav_sampwidth = f.getsampwidth()
        '''
        print("nFrame: " + str(f.getnframes()),
              "framerate: " + str(f.getframerate()),
              "comptype: " + str(f.getcomptype()),
              "nchannels: " + str(f.getnchannels()),
              "compname: " + str(f.getcompname()),
              "sampwidth: " + str(f.getsampwidth()),
              )


print("Wav didn't load \n" + str(get_properties(wav_error)))
print("Wav does load \n" + str(get_properties(wav_loads)))
