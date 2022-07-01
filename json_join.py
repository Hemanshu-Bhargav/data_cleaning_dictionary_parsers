import json

#files=['dataset.json','valid.json', 'test.json']
files=['dataset.json', 'test.json']

def merge_JsonFiles(filename):
    result = {}
    for f1 in filename:
        with open(f1, 'r+') as infile:
            result.update(json.load(infile))
            infile.seek(0)

    with open('train.json', 'w') as output_file:
        json.dump(result, output_file, indent=2)

merge_JsonFiles(files)
