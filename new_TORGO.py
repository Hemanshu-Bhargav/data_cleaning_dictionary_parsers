import os
import shutil
import json
import wave
import contextlib


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


'''Copy the audio file from /extracted to /sorted and rename it with the dataset prefix'''
def c_p(src_file, src_filename, dst_path, dst_filename):
    """
    c_p is called in sortDataset() as so:
    c_p(tempWavFile,
        transcript.replace('.txt', '.wav'),
        destPath,
        speakerID+transcript.replace('.txt', '.wav')
        )
    :param src_file: tempWavFile = Dysarthric_Processing_Hemanshu\code\datasets\extracted\TORGO\F01\Session1\wav_headMic\0001.wav
    :param src_filename: transcript.replace('.txt', '.wav') = 0001.wav (from 0001.txt)
            (in /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/prompts/ but transcript only holds 0001.wav, 0002.wav etc)
    :param dst_path: destPath = C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code/datasets/sorted/TORGO
    :param dst_filename: speakerID+transcript.replace('.txt', '.wav') = /TORGO_F01_Session1_0001.wav
    :return:
    """

    '''copy /Dysarthric_Processing_Hemanshu/code/datasets/extracted/TORGO/F01/Session1/wav_headMic/0001.wav
       to /Dysarthric_Processing_Hemanshu/code/datasets/sorted/TORGO so we get
       a copied audio file /Dysarthric_Processing_Hemanshu/datasets/sorted/TORGO/0001.wav'''
    shutil.copy2(src_file, dst_path)
    '''Create a new filename called dst_file which is the join of /Dysarthric_Processing_Hemanshu/datasets/sorted/TORGO/
       and 0001.wav resulting in /Dysarthric_Processing_Hemanshu/datasets/sorted/TORGO/0001.wav
       This is the filename for the file copied using shutil.copy2'''
    dst_file = os.path.join(dst_path, src_filename)
    # print(dst_file)
    '''The new destination filename is the join of /Dysarthric_Processing_Hemanshu/datasets/sorted/TORGO/0001.wav and 
       /TORGO_F01_Session1_0001.wav to get /Dysarthric_Processing_Hemanshu/datasets/sorted/TORGO/TORGO_F01_Session1_0001.wav'''
    new_dst_file_name = os.path.join(dst_path, dst_filename)
    # print(new_dst_file_name)
    '''Rename /Dysarthric_Processing_Hemanshu/datasets/sorted/TORGO/0001.wav to 
       /Dysarthric_Processing_Hemanshu/datasets/sorted/TORGO/TORGO_F01_Session1_0001.wav '''
    os.rename(dst_file, new_dst_file_name)
    print(dst_filename)
    '''Return TORGO_F01_Session1_0001.wav'''
    duration_wavefilename = dst_filename
    return (dst_filename)


def sortDataset():
    print('')
    '''For each person F01 to M05 in /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO'''
    for person in os.listdir(sourcePath):
        '''For each session directory (ignoring the 'Notes' directories) in /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01'''
        for session in os.listdir(os.path.join(sourcePath, person)):
            if session != "Notes":

                ''' The dataset hierarchy for transcripts is person -> session -> prompts
                The dataset hierarchy for headMic recordings is person -> session -> wav_headMic
                The dataset hierarchy for headMic recordings is person -> session -> wav_arrayMic
                We need to join headMic and arrayMic to create wav samples for the JSON manifest files.
                
                wordsPath = /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/prompts
                wavFilePath = /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/wav_headMic
                wavFileAltPath = /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/wav_arrayMic'''

                wordsPath = os.path.join(sourcePath,person,session,'prompts')
                #print("wordsPath is " + str(wordsPath))
                wavFilePath = os.path.join(sourcePath,person,session,'wav_headMic')
                wavFileAltPath = os.path.join(sourcePath,person,session,'wav_arrayMic')

                '''Set speakerID to /TORGO_F01_Session01_ so that it can be joined with the existing wave file name (trailing _ allows easy concatenation
                   with transript txt file a few lines below)'''
                speakerID = dataset+'_'+person+'_'+session+'_'
                #print("SpeakerID is " + str(speakerID))
                ''' words = list of .txt transcripts in /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/prompts for that speaker
                    ex. 001.txt, 002.txt etc.'''
                words = os.listdir(wordsPath)
                #print("Words is " + str(words))

                '''For each transcript do the following. Enumerate is just to track files using filenumber iterator variable'''
                for fileNumber, transcript in enumerate(words):

                    #print("Transcript is " + str(transcript))
                    #print("speakerID+transcript is " + str(speakerID+transcript.replace('.txt', 'wav')))
                    '''With /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/prompts/001.txt open as f'''
                    with open(os.path.join(wordsPath,transcript)) as f:

                        '''Create a JSON tri_entry using speakerID+001 instead of speakerID+001.txt. Ex. /TORGO_F01_Session01_001
                           The tri_entry for words is the entire file (read with readlines()) with any trailing whitespaces removed (using rstrip())
                        '''
                        train_json_entries_dictionary[speakerID+transcript.replace('.txt', '')]['words'] = \
                            {
                            "words": f.readlines()[0].rstrip()
                            }
                        #words_placeholder = []
                        #words_placeholder.append(f.readlines()[0].rstrip())
                    '''tempWavFile = /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/wav_headMic/001.wav
                       We replace transcript with .wav instead of reading the directory for convenience since the files have the same nomenclature'''
                    tempWavFile=os.path.join(wavFilePath,transcript.replace('.txt', '.wav'))
                    #print("tempWavFile is " + str(tempWavFile))

                    '''If /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/wav_headMic/001.wav exists '''
                    if os.path.isfile(tempWavFile):
                        ''' newfile = TORGO_F01_Session1_0001.wav '''
                        newfile = c_p(tempWavFile, transcript.replace('.txt', '.wav'), destPath, speakerID+transcript.replace('.txt', '.wav'))
                        print("Newfile initially assigned to" + str(newfile))
                        '''json tri_entry [TORGO_F01_Session1_0001] = { "file" : TORGO_F01_Session1_0001.wav} '''
                        wav_path = os.path.join(sourcePath, person, tempWavFile)
                        print("wav_path is " + str(wav_path))
                        '''
                        train_json_entries_dictionary[speakerID+transcript.replace('.txt', '')] =\
                            {
                            "wav" : newfile,
                            "length": get_duration(wav_path)
                            } 
                        '''
                        google_colab_path = "/content/drive/MyDrive/TORGO/" + newfile
                        train_json_entries_dictionary[speakerID+transcript.replace('.txt', '')]['wav'] = google_colab_path
                        train_json_entries_dictionary[speakerID+transcript.replace('.txt', '')]['length'] = get_duration(wav_path)
                        #for i in words_placeholder:
                        #    train_json_entries_dictionary[speakerID+transcript.replace('.txt', '')]['words'] = words_placeholder[i]
                    else:
                        # print(transcript.replace('.txt', '.wav') + " was not found in wav_headMic/, checking wav_arrayMic/...", end = '')
                        '''tempWavFile = /Dysarthric_Processing_Hemanshu/datasets/extracted/TORGO/F01/session/wav_arrayMic/0001.wav '''
                        tempWavFile = os.path.join(wavFileAltPath,transcript.replace('.txt', '.wav'))
                        print("New tempWavFile is " + str(tempWavFile))
                        if os.path.isfile(tempWavFile):
                            '''Reassign newfile to TORGO_F01_Session1_0001.wav'''
                            google_colab_path = c_p(tempWavFile, transcript.replace('.txt', '.wav'), destPath, speakerID+transcript.replace('.txt', '.wav'))
                            print("Newfile has been reassigned to google_colab_path" + str(google_colab_path))
                            train_json_entries_dictionary[speakerID+transcript.replace('.txt', '')] =\
                                {
                                "file" : google_colab_path
                                }
                            # print(" found, storing this record.")
                        else:
                            # print(" not found, skipping this record")
                            break

                        ''' Progress: ex. F02: 1824 of 4859: 37% complete '''
                    print(person+" --> "+session+": "+ str(fileNumber+1) + " of " + str(len(words)) + " : " + str(int((100*(fileNumber+1))/len(words)))+ "% complete", end='\r')
                    print('')
    jsonFile = open(os.path.join(destPath, "dataset.json"), 'w')
    jsonFile.write(json.dumps(train_json_entries_dictionary))
    print('wrote dataset mapping to', os.path.join(destPath, "dataset.json"))


''' _______________________________________________________________________________________________________
Set Path Definitions
The default path definition is the current working directory C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code
 + code/datasets resulting in C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code/datasets
 
dataset = TORGO, again for modularity

sourcePath = C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code/datasets + ../datasets/extracted + ../extracted/TORGO
resulting C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code/datasets/extracted/TORGO

destPath = C:/Users/Hemanshu/Desktop/dysarthria_speechbrain-main/Dysarthric_Processing_Hemanshu/code/datasets/sorted/TORGO
'''
path = os.path.join(os.getcwd(), 'datasets')
dataset = 'TORGO'

sourcePath = os.path.join(path, 'extracted', dataset)
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
