import os
import shutil
import json
import fnmatch
import wave
import contextlib

def get_duration(sourcePath):
    for person in os.listdir(sourcePath):
        wavFiles = fnmatch.filter(os.listdir(os.path.join(sourcePath, person)), "*.wav")
        for tempWavFile in wavFiles:
            wav_path = os.path.join(sourcePath, person, tempWavFile)
            with contextlib.closing(wave.open(wav_path,'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                #duration = signal.shape[0] / 16000
                #with wave.open(wav_path, 'rb') as f: #f.close()
                print("Duration in seconds is: " + str(duration))
    return duration


def c_p(src_file, src_filename, dst_path):
    shutil.copy2(src_file, dst_path)
    dst_file = os.path.join(dst_path, src_filename)
    return dst_file


path = os.path.join(os.getcwd(),'datasets')
dataset = 'UASpeech'
sourcePath = os.path.join(path, 'extracted', dataset, 'audio')
datasetPath = os.path.join(path, 'extracted', dataset, 'mlf')
destPath = os.path.join(path, 'sorted', dataset)

''' Save all file/duration/text entries here. This json dictionary outputs to train.json'''
train_json_entries_dictionary = {}

'''Delete any previous sorted directory and start fresh'''
if os.path.exists(destPath):
    shutil.rmtree(destPath)
os.mkdir(destPath)
os.chmod(destPath, 0o777)

'''Run the script and build train.json'''
for person in os.listdir(sourcePath):
    wavFiles = fnmatch.filter(os.listdir(os.path.join(sourcePath, person)), "*.wav")
    print(wavFiles)
    for tempWavFile in wavFiles:
        c_p(os.path.join(sourcePath, person, tempWavFile),tempWavFile,destPath)
        get_duration(sourcePath)
