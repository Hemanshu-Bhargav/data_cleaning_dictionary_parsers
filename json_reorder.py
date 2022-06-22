import json
import os

with open("dataset.json", "r") as jsonFile:
    torgo_train = json.load(jsonFile)
    #print(torgo_train)
    with open("train.json", "w") as train:
        for entry in train:

            json.dump(torgo_train, ["wav", "length", "words"])

        with open("unprocessed_valid.json", "r+") as f:
            json_to_dictionary = json.load(f)
            for speakerID in list(json_to_dictionary.keys()):
                for inner_entry in list(json_to_dictionary[speakerID].values()):
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

