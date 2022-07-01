import json

to_exclude1 = "jpg"
to_exclude2 = "["
file_list = []


def json_cleaner():
    with open("test.json", "r+") as f:
        json_to_dictionary = json.load(f)
        for speakerID in list(json_to_dictionary.values()):
            print("SpeakerID " + str(speakerID) + " has a wav file of duration speakerID " + speakerID["length"])
            '''
            words, length, wav = speakerID["words"], speakerID["length"], speakerID["wav"]
            del speakerID["words"]
            del speakerID["length"]
            del speakerID["wav"]
            speakerID["wav"] = wav
            speakerID["length"] = length
            speakerID["words"] = words
            '''