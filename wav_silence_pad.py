from pydub import AudioSegment
import librosa
import wave
import soundfile as sf
import os
# ffmpeg and sndfile must also be installed

pad_ms = 1000  # milliseconds of silence needed
silence = AudioSegment.silent(duration=pad_ms)

datasets_dir = "test"

path_dir = os.path.join(os.getcwd(), "datasets/sorted/", datasets_dir)

for each_wav in os.listdir(path_dir):
    filename = os.path.join(path_dir, os.path.splitext(each_wav)[0])
    x, _ = librosa.load(each_wav, sr=16000)
    with open(each_wav, "r") as fr:
        audio = AudioSegment.from_wav(fr)
    with open(each_wav, "w") as fw:
        padded = audio + silence  # Adding silence after the audio
        fixed_wav = padded.export(filename, format='wav')
        sf.write(fixed_wav, x, 16000)