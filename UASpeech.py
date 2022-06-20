import os
import shutil
import json
import fnmatch
import wave
import contextlib


def get_duration(wav_path):
    with contextlib.closing(wave.open(wav_path,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print("Duration in seconds is: " + str(duration))
    return duration


'''Copy the audio file from /extracted to /sorted and rename it with the dataset prefix'''
def c_p(src_file, src_filename, dst_path, dst_filename):
    ''' shutil.copy2 https://docs.python.org/3/library/shutil.html#shutil.copy
    Copies the file src to the file or directory dst.
    src and dst should be path-like objects or strings.
    If dst specifies a directory, the file will be copied into dst using the base filename from src.
    If dst specifies a file that already exists, it will be replaced. Returns the path to the newly created file

    c_p is called in sortDataset() as so:
    c_p(
                    os.path.join(sourcePath, person, tempWavFile),
                    tempWavFile,
                    destPath,
                    newfilename
                )
    # os.path.join(/Dysarthric_Processing_Hemanshu/datasets/extracted/UASpeech/audio, person, tempWavFile)
    person = directories named F01 to M16
    tempWavFile = the iterated audio files from /extracted: ex. F02_B1_C1_M2.wav
    newfilename = newfilename = /+ dataset + '_' + tempWavFile + / = /UASpeech_F02_B1_C1_M2.wav

    :param src_file: /Dysarthric_Processing_Hemanshu/datasets/extracted//UASpeech/audio/F02/F02_B1_C1_M2
    :param src_filename: F02_B1_C1_M2.wav
    :param dst_path: destPath = /Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech
    :param dst_filename: /UASpeech_F02_B1_C1_M2.wav
    :return: /UASpeech_F02_B1_C1_M2.wav
    '''

    '''copy /Dysarthric_Processing_Hemanshu/datasets/extracted//UASpeech/audio/F02/F02_B1_C1_M2 
       to Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech so we get
       a copied audio file Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech/F02_B1_C1_M2'''
    shutil.copy2(src_file, dst_path)
    '''Create a new file called dst_file which is the join of Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech
       and F02_B1_C1_M2 or Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech/F02_B1_C1_M2'''
    dst_file = os.path.join(dst_path, src_filename)
    # print(dst_file)
    '''The new destination file is the join of Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech and 
       /UASpeech_F02_B1_C1_M2 to get Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech/UASpeech_F02_B1_C1_M2'''
    new_dst_file_name = os.path.join(dst_path, dst_filename)
    # print(new_dst_file_name)
    '''Rename Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech/F02_B1_C1_M2 to 
       Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech/UASpeech_F02_B1_C1_M2 '''
    os.rename(dst_file, new_dst_file_name)
    print(dst_filename)
    '''Return Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech/UASpeech_F02_B1_C1_M2'''
    duration_wavefilename = dst_filename
    return (dst_filename)


def convertmlftocsv(path):
    mlfreader = open(path, "r")
    mlflist = mlfreader.read() \
        .replace('#!MLF!#', '') \
        .replace('.\n', '[endofline]') \
        .replace('\n', '') \
        .replace('[endofline]', '\n') \
        .replace('"*/', '') \
        .replace('.lab"', ' ') \
        .splitlines()

    mlfdict = {}

    for line in mlflist:
        linelist = line.split()
        mlfdict[linelist[0]] = ' '.join(linelist[1:])

    # print(mlfdict) #Format is {'Person_Session_Wav': 'Transcript', 'Person_Session_Wav2': 'Transcript2'}
    return mlfdict


def sortDataset():
    print('')
    '''For each directory F02-M16 in the list of directories from /Dysarthric_Processing_Hemanshu/datasets/extracted/UASpeech/audio'''
    for person in os.listdir(sourcePath):
        try:
            '''tempdataset = join /Dysarthric_Processing_Hemanshu/datasets/extracted/UASpeech/mlf, F02, F02_word.mlf
               F02_word.mlf is a file within the extracted/UASpeech/mlf/F02 directory
               tempdataset = /Dysarthric_Processing_Hemanshu/datasets/extracted/UASpeech/mlf/F02/F02_word.mlf
            '''
            tempdataset = os.path.join(datasetPath, person, person + '_word.mlf')
            # print(tempdataset)
            '''oldtrain_json_entries_dictionary = dictionary of filenames and transcriptions for each person
               ex. {...'F02_B2_UW77_M5': 'DISPOSSESS', 'F02_B3_UW93_M3': 'GLASSES'}
                   {'F03_B3_UW6_M8': 'GREYHOUND', 'F03_B2_UW90_M5': 'CARROT',...} so 1 dictionary per person per iteration
                   (one iteration of the loop creates one dictionary for each person's transcriptions and the associated
                   speaker/session ID)
            '''
            oldtrain_json_entries_dictionary = convertmlftocsv(tempdataset)
            #print(oldtrain_json_entries_dictionary)

            '''
            Create a LIST (ADT) of all the wave files which match .wav in the list of files under 
            /Dysarthric_Processing_Hemanshu/datasets/extracted/UASpeech/audio/F02
            So 1 audio sample list per person per iteration. https://docs.python.org/3/library/fnmatch.html
            Construct a list from those elements of the iterable names that match pattern. 
            It is the same as [n for n in names if fnmatch(n, pattern)], but implemented more efficiently.
            '''
            wavFiles = fnmatch.filter(os.listdir(os.path.join(sourcePath, person)), "*.wav")
            # print(wavFiles)

            '''for each wave file STRING (ex. F02_B1_C1_M2.wav). Enumerate is just to track files using filenumber iterator variable'''
            for filenumber, tempWavFile in enumerate(wavFiles):
                #print(type(tempWavFile)) <class 'str'>
                '''speakerID = replace F02_B1_C1_M2.wav with F02_B1_C1_M2'''
                speakerID = tempWavFile.replace('.wav', '')
                '''newfilename just adds dataset prefix = /UASpeech_F02_B1_C1_M2.wav'''
                newfilename = \
                    dataset + '_' + \
                    tempWavFile
                '''Return Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech/UASpeech_F02_B1_C1_M2'''
                c_p(
                    os.path.join(sourcePath, person, tempWavFile),
                    tempWavFile,
                    destPath,
                    newfilename
                )
                #get_duration(c_p(os.path.join(sourcePath, person, tempWavFile),tempWavFile,destPath,newfilename))
                # print(type(new_wav)). new_wav = c_p is also a string return value
                '''JSON dict = { speakerID {
                                            wav:
                                            length
                                            words
                                            }, speakerID2'''
                wav_path = os.path.join(sourcePath, person, tempWavFile)
                google_colab_path = "/content/drive/MyDrive/UASpeech/" + newfilename
                print("Path for google_colab_path field path is " + google_colab_path)
                try:
                    print("dst_filename")
                    train_json_entries_dictionary[speakerID] = {
                        "wav": google_colab_path,
                        "length": get_duration(wav_path),
                        "words": oldtrain_json_entries_dictionary[speakerID]
                    }
                    ''' Progress: ex. F02: 1824 of 4859: 37% complete '''
                    print(person + ": " + str(filenumber + 1) + " of " + str(len(wavFiles)) + " : " + str(
                        int((100 * (filenumber + 1)) / len(wavFiles))) + "% complete", end='\r')
                except:
                    do = "nothing"

        except FileNotFoundError:
            print("File Not Found:", dataset)
        print('')

    jsonFile = open(os.path.join(destPath, "dataset.json"), 'w')
    jsonFile.write(json.dumps(train_json_entries_dictionary, indent=2))
    print('wrote dataset mapping to', os.path.join(destPath, "dataset.json"))


duration_wavefilename = ""
'''
 Set path definitions
 The default path is the upper directory (Desktop\dysarthria_speechbrain-main\Dysarthric_Processing_Hemanshu\code.
 Join this directory (/Dysarthric_Processing_Hemanshu, the directory above code) with the datasets directory
 (/Dysarthric_Processing_Hemanshu/datasets which contains /sorted and /extracted).
 path = /Dysarthric_Processing_Hemanshu/datasets
 
 Set dataset variable to UASpeech (just a global variable to avoid hard-coding)
'''
path = os.path.join(os.getcwd(), 'datasets')
dataset = 'UASpeech'

'''
Next, join /Dysarthric_Processing_Hemanshu/datasets with /datasets/extracted, the directory /extracted/UASpeech
(in both cases of 'extracted' and dataset, a string is passed but these are directories) and extracted/UASpeech/audio
resulting in sourcePath = /Dysarthric_Processing_Hemanshu/datasets/extracted/UASpeech/audio which holds the audio files

Then join /Dysarthric_Processing_Hemanshu/datasets with datasets/extracted, extracted/UASpeech and UASpeech/mlf
resulting in datasetPath = /Dysarthric_Processing_Hemanshu/datasets/extracted//UASpeech/mlf which holds the transcripts

Finally join /Dysarthric_Processing_Hemanshu/datasets with /datasets/sorted and /sorted/UASpeech
Note: At this point /sorted/UASpeech doesn't exist, but is created (or deleted and created rather) about 3 lines down
destPath = /Dysarthric_Processing_Hemanshu/datasets/sorted/UASpeech (this is where the cleaned dataset is built)
'''
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
sortDataset()

'''
Note: All comments use Linux filesystem syntax to be consistent w/ Google Colab. So 
Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code
instead of Windows appropriate:
Desktop\dysarthria_speechbrain-main\Dysarthric_Processing_Hemanshu\code
'''
