#import string
from collections import OrderedDict
import json

to_exclude1 = "jpg"
to_exclude2 = "["
file_list = []
# If words field contains exclusion criteria, delete the JSON speakerID key-value pair

def file_test():
    with open("transcript_test_file.txt", "r") as f:
        file_list = f.readlines()
        #print(file_list)
        for list_item in file_list:
            print(list_item)
            if to_exclude1 in list_item:
                print("String match successful")
            if to_exclude2 in list_item:
                print("String match 2 successful")


def json_cleaner():
    with open("mid_processed_valid.json", "r+") as f:
        json_to_dictionary = json.load(f)
        for speakerID in list(json_to_dictionary.keys()):
            for inner_entry in list(json_to_dictionary[speakerID].values()):
                if isinstance(inner_entry, str):
                    if to_exclude1 in inner_entry:
                        print(str(speakerID))
                        json_to_dictionary.pop(speakerID)
                    if to_exclude2 in inner_entry:
                        print(str(speakerID))
                        json_to_dictionary.pop(speakerID)
        inner_key_order = ("wav", "length", "words")
        #for speakerID in json_to_dictionary:
        #json_to_dictionary[speakerID] = [ordered(entry, inner_key_order) for entry in json_to_dictionary[speakerID]]
        json_to_dictionary[speakerID] = [ordered(entry, json_to_dictionary[speakerID][2][1][0]) for entry in json_to_dictionary[speakerID]]

        #for speakerID in list(json_to_dictionary):
            #print(json_to_dictionary[speakerID])  #print(json_to_dictionary[speakerID].keys())   #print(json_to_dictionary[speakerID].values())
            #cleaned_dictionary = json_to_dictionary[speakerID].copy()
            #print(cleaned_dictionary)
        '''
        words, wav = json_to_dictionary[speakerID]['words'], json_to_dictionary[speakerID]['wav']
        del json_to_dictionary[speakerID]['words']
        del json_to_dictionary[speakerID]['wav']
        json_to_dictionary[speakerID]['wav'] = wav
        json_to_dictionary[speakerID]['words'] = words
        
        json_to_dictionary[speakerID]['words'], json_to_dictionary[speakerID]['wav'] = json_to_dictionary[speakerID]['wav'], json_to_dictionary[speakerID]['words']
        
        for inner_dictionary in cleaned_dictionary:
            # inner_dictionary = {'words': 'stick', 'length': 1.399375, 'wav': '/content/drive/MyDrive/TORGO/TORGO_F01_Session1_0006.wav'}
            words, wav = inner_dictionary['words'], inner_dictionary['wav']
            del inner_dictionary['words']
            del inner_dictionary['wav']
            inner_dictionary['wav'] = wav
            inner_dictionary['words'] = words
        '''
                # Tuple Unpacking for efficient swap
                #inner_entry['words'], inner_entry['wav'] = inner_entry['wav'], inner_entry['words']
                #inner_entry[0], inner_entry[2] = inner_entry[2], inner_entry[0]
                #json_to_dictionary['length'], json_to_dictionary['words'] = json_to_dictionary['words'], json_to_dictionary['length']
    jsonFile = open("valid.json", 'w')
    jsonFile.write(json.dumps(json_to_dictionary, indent=2))

def ordered(d, desired_key_order):
    return OrderedDict([(key, d[key]) for key in desired_key_order])

json_cleaner()

