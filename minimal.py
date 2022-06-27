import json

to_exclude1 = "jpg"
to_exclude2 = "["
file_list = []


def json_cleaner():
    with open("mid_processed_valid.json", "r+") as f:
        json_to_dictionary = json.load(f)
        for speakerID in list(json_to_dictionary.values()):
            print(speakerID["length"])
            words, length, wav = speakerID["words"], speakerID["length"], speakerID["wav"]
            del speakerID["words"]
            del speakerID["length"]
            del speakerID["wav"]
            speakerID["wav"] = wav
            speakerID["length"] = length
            speakerID["words"] = words
    jsonFile = open("valid.json", 'w')
    jsonFile.write(json.dumps(json_to_dictionary, indent=2))

def exclusion_criteria():
    check = "length"
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
    jsonFile = open("mid_processed_valid.json", 'w')
    jsonFile.write(json.dumps(json_to_dictionary, indent=2))


exclusion_criteria()
json_cleaner()
