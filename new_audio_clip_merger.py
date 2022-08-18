import wave
import os
from pydub import AudioSegment

datasets_dir = "test_dataset"
path_dir = os.path.join(os.getcwd(), "datasets/sorted/", datasets_dir)
# initialize a counter to keep track of every four files; whatever is left over is omitted
count = 0
merged_name = ""
merged_counter = 0
exempt = ".DS_Store"
merged_file = AudioSegment.empty()

for each_wav in os.listdir(path_dir):
    path_to_open_each_wav = os.path.join(path_dir, each_wav)
    filename = path_dir + os.path.join(path_dir, os.path.splitext(each_wav)[0])
    print("This is the filename" + filename)
    if exempt in filename:
        pass
    else:
        count += 1
        audio_in_file = os.path.join(path_dir, os.path.splitext(each_wav)[0])
        audio_out_file = str(audio_in_file) + str(os.path.splitext(each_wav)[-1])
        if count == 1:
            temp_merge1 = AudioSegment.from_wav(path_to_open_each_wav)
        if count == 2:
            temp_merge2 = AudioSegment.from_wav(path_to_open_each_wav)
        if count == 3:
            temp_merge3 = AudioSegment.from_wav(path_to_open_each_wav)
        if count == 4:
            merged_counter += 1
            # New name is UASpeech_New_1 and increments by 1
            merged_name = "UASpeech_New_" + str(merged_counter) + ".wav"
            print("The name of the new merged file if created would be" + merged_name)
            merged_file = temp_merge1 + temp_merge2 + temp_merge3 + AudioSegment.from_wav(path_to_open_each_wav)
            merged_file.export(os.path.join(path_dir, merged_name), format="wav")
            # reset counter to perform above operations every fourth iteration
            # alternatively can use modulus operation but raises space/time complexity
            count = 0

