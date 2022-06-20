import string
import json
#open and load json file

to_exclude1 = "jpg"
to_exclude2 = "["
file_list = []
# If words field contains exclusion criteria, delete the JSON speakerID key-value pair
#test_string1 = "input/images/kitchen.jpg"
#test_string2 = "tear [as in tear up]"

# extract outerkey (speakerID) and words field
# save speakerIDs in

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
    with open("valid.json", "r+") as f:
        json_to_dictionary = json.load(f)
        for speakerID in json_to_dictionary.keys():
            for inner_entry in json_to_dictionary[speakerID].values():
                #print(type(inner_entry))
                #print(inner_entry)
                #for entry_value in inner_entry:
                if isinstance(inner_entry, str):
                    if to_exclude1 in inner_entry:
                        print(str(speakerID))
                        json_to_dictionary.pop(speakerID)
                    if to_exclude2 in inner_entry:
                        print(str(speakerID))
                        json_to_dictionary.pop(speakerID)


json_cleaner()
