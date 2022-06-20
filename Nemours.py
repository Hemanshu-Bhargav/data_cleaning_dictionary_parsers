import os
import shutil
import json
import fnmatch
import wave
import contextlib


def c_p(src_file, src_filename, dst_path, dst_filename):
    '''
    :param src_file: /Dysarthric_Processing_Hemanshu/datasets/extracted//Nemours/SENT/BB/BB.wav
    :param src_filename:
    :param dst_path: Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours
    :param dst_filename:
    :return:
    '''


    '''copy /Dysarthric_Processing_Hemanshu/datasets/extracted//Nemours/SENT/BB/BB.wav
    to Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours so we get a copied audio file
    Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours/BB.wav'''
    shutil.copy2(src_file, dst_path)

    '''Create a new file called dst_file which is the join of Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours
    and BB.wav or Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours/BB.wav '''

    dst_file = os.path.join(dst_path, src_filename)
    # print(dst_file)

    '''The new destination file is the join of Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours and 
    /Nemours_BB.wav to get Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours/Nemours_BB.wav'''

    '''Rename Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours/BB.wav to 
    Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours/Nemours_BB.wav'''

    os.rename(dst_file, new_dst_file_name)
    print("dst_filename is " + str(dst_filename))
    '''Return Dysarthric_Processing_Hemanshu/datasets/sorted/Nemours/Nemours_BB.wav '''
    return (dst_filename)


def get_duration(wav_path):
    with contextlib.closing(wave.open(wav_path,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print("Duration in seconds is: " + str(duration))
    return duration


#_____________________________________________________PARAGRAPH____________________________________________
paragraphpath = os.path.join(datasets, "PARA")

personfiles = os.listdir(paragraphpath)
for person in personfiles:
    #file: audio

#______________________________________________________SENTENCE_____________________________________________

sentencepath = os.path.join(datasets, "SENT")

for person in os.listdir(sentencepath):
    session = os.path.join(person, sentencepath)
    print(session)
    for wav_text_directories in session:
        person_path = os.path.join(sentencepath, person, session)

        wav_sent_path = os.path.join(person_path, "WAV")

        words_sent_path = os.path.join(sentencepath, "TXT")

        c_p(wav_sent_path, destinationPath, dst_path, dst_filename)
        #Json = { audio, text}
