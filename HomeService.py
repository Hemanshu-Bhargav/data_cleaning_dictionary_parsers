import os
import shutil
import json
import wave
import contextlib
import csv

''' C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code/datasets '''
path = os.path.join(os.getcwd(), 'datasets')
dataset = 'HomeService'

''' sourcePath = C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code/datasets/extracted/HomeService '''
sourcePath = os.path.join(path, 'extracted', dataset)
''' destPath = C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code/datasets/sorted/HomeService '''
destPath = os.path.join(path, 'sorted', dataset)

'''oldMappingsFile = dictionary at /Dysarthric_Processing_Hemanshu/code/datasets/extracted/HomeService/tran/homeServiceV11-asr.txt'''
oldMappingsFile = os.path.join(sourcePath, "tran", "homeServiceV11-asr.txt")
oldMappings = {}

train_json_entries_dictionary = {}

if os.path.exists(destPath):
    shutil.rmtree(destPath)
os.mkdir(destPath)
os.chmod(destPath, 0o777)

def get_duration(wav_path):
    try:
        with contextlib.closing(wave.open(wav_path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            print("Duration in seconds is: " + str(duration))
            return duration
    except EOFError as e:
        print(e)

'''Get all transcripts from homeServiceV11-asr.txt (also has speakerIDs preceeding transcript per line)  '''
def retrieveWords():
    '''
    Open /Dysarthric_Processing_Hemanshu/code/datasets/extracted/HomeService/tran/homeServiceV11-asr.txt
    as a csv but space delimited instead of comma separated
    '''
    with open(oldMappingsFile, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        '''Remove hom- prefix from each speakerID and transcript combo (1 per line)'''
        for line in csv_reader:
            oldMappings[line[0].replace("hom-", '')] = line[1]

def sortDataset():
    print('')
    '''for each speaker in /Dysarthric_Processing_Hemanshu/code/datasets/extracted/HomeService/audio'''
    for person in os.listdir(os.path.join(sourcePath, "audio")):
        '''for each session listed under F01 to M03 (1-2 labelled ER01 and ID01'''
        for session in os.listdir(os.path.join(sourcePath, "audio", person)):
            '''Store all audio samples from /extracted/HomeService/audio/F01/ER01 in wavFiles'''
            wavFiles = os.listdir(os.path.join(sourcePath, "audio", person, session))
            '''For each wav file do the following (since we have a transcript dictionary). Track w/ Enumerate & filenumber'''
            for fileNumber, tempWavFile in enumerate(wavFiles):
                ''' remove hom- prefix and .wav extension for speakerID '''
                speakerID = tempWavFile.replace('.wav', '').replace("hom-", '')
                ''' newfilename = HomeService_F01_ER01_MCW0000045000001.wav  (speakerID with .wav removed) '''
                newfilename = \
                    dataset+'_'+\
                    person+'_'+\
                    session+'_'+\
                    tempWavFile.replace('.wav', '')\
                    .replace("hom-", '')\
                    .replace(person, '')\
                    .replace(session, '')\
                    + ".wav"
                '''  '''
                c_p(
                    os.path.join(sourcePath, "audio", person, session, tempWavFile),
                    tempWavFile,
                    destPath,
                    newfilename
                )
                wav_path = os.path.join(sourcePath, "audio", person, session, tempWavFile)
                google_colab_path = "/content/drive/MyDrive/HomeService/" + newfilename
                train_json_entries_dictionary[speakerID] = {
                    "file": google_colab_path,
                    "words": oldMappings[speakerID],
                    "length": get_duration(wav_path)
                }
                print(person+" --> "+session+": "+ str(fileNumber+1) + " of " + str(len(wavFiles)) + " : " + str(int((100*(fileNumber+1))/len(wavFiles)))+ "% complete", end='\r')
            print('')
    jsonFile = open(os.path.join(destPath, "dataset.json"), 'w')
    jsonFile.write(json.dumps(train_json_entries_dictionary))
    print('wrote dataset mapping to', os.path.join(destPath, "dataset.json"))


def c_p(src_file, src_filename, dst_path, dst_filename):
    '''
    :param src_file: os.path.join(sourcePath, "audio", person, session, tempWavFile)
                            = Dysarthric_Processing_Hemanshu/code/datasets/extracted/HomeService/F01/ER01/
    :param src_filename: tempWavFile =
    :param dst_path: destPath = /Dysarthric_Processing_Hemanshu/code/datasets/sorted/HomeService
    :param dst_filename: newfilename =
    :return:
    '''
    shutil.copy(src_file, dst_path)
    dst_file = os.path.join(dst_path, src_filename)
    new_dst_file_name = os.path.join(dst_path, dst_filename)
    os.rename(dst_file, new_dst_file_name)
    return(dst_filename)


retrieveWords()
sortDataset()
