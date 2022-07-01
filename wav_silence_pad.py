from pydub import AudioSegment
import librosa
import wave
import soundfile as sf
import os
import contextlib
from scipy.io import wavfile
# ffmpeg and sndfile must also be installed

datasets_dir = "test"
path_dir = os.path.join(os.getcwd(), datasets_dir)
os.chmod(os.getcwd(), 0o777)
os.chmod(path_dir, 0o777)
#print(os.listdir(path_dir))

def silence_padder(path_dir):
    pad_ms = 1000  # milliseconds of silence needed
    silence = AudioSegment.silent(duration=pad_ms)
    for each_wav in os.listdir(path_dir):
        #filename = os.path.join(os.getcwd(),"datasets/sorted/", datasets_dir, os.path.splitext(each_wav)[0])
        #filename = os.path.splitext(each_wav)[0]
        filepath = os.path.join(path_dir,each_wav)
        with open(filepath,'rb') as fr:
            audio = AudioSegment.from_wav(fr)
        with open(filepath,'wb') as fw:
            padded = audio + silence  # Adding silence after the audio
            fixed_wav = padded.export(each_wav, format='wav')


def wav_format_correction(path_dir):
    for each_wav in os.listdir(path_dir):
        filepath = os.path.join(path_dir,each_wav)
        #x, _ = wavfile.read(filepath)
        x, _ = sf.read(filepath)
        #x, _ = librosa.load(filepath, sr=16000)
        sf.write(each_wav, x, 16000)
    '''
    with contextlib.closing(open(filepath,'r', encoding="latin-1")) as fr:
    audio = AudioSegment.from_wav(fr)
    with contextlib.closing(open(filepath,'w', encoding="latin-1")) as fw:
    padded = audio + silence  # Adding silence after the audio
    fixed_wav = padded.export(filename, format='wav')
    sf.write(fixed_wav, x, 16000)
    '''
wav_format_correction(path_dir)
silence_padder(path_dir)

'''
path_dir = os.path.join(os.getcwd(), "datasets", "sorted", datasets_dir)
for each_wav in os.listdir(path_dir):
    filename = os.path.join(path_dir, os.path.splitext(each_wav)[0])
    x, _ = librosa.load(each_wav, sr=16000)
    with open(each_wav, "r") as fr:
        audio = AudioSegment.from_wav(fr)
    with open(each_wav, "w") as fw:
        padded = audio + silence  # Adding silence after the audio
        fixed_wav = padded.export(filename, format='wav')
        sf.write(fixed_wav, x, 16000)
'''
