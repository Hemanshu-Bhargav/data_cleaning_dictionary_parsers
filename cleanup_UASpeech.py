import os
import json
import contextlib


path = os.path.join(os.getcwd(), "datasets\\sorted\\UASpeech")
json_path = os.path.join(path, "train.json")
os.chmod(path, 0o777)

list_of_wav = []
collection_of_speakerID = {}

with contextlib.closing(open(json_path, "r")) as train_json:
    # Converts to dictionary
    train_dictionary = json.load(train_json)
    #print("Train dictionary is of type" + str(type(train_dictionary)))
    # access speakerID and file value
    for speakerID in train_dictionary:
        #print(speakerID)
        collection_of_speakerID.keys()
        for tri_entry in speakerID:
            file_path = os.path.join(path, tri_entry)
            #print("File" + str(file) + "\n belongs to speakerID" + str(speakerID))
            if not os.path.isfile(file_path):
                print(str(train_dictionary.keys()))
                #list_of_wav.append(file_path)
            else:
                continue
                #train_dictionary.pop(file_path)
#print(list_of_wav)
