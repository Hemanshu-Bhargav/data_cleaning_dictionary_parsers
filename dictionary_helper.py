def invert(cacm):
            #Create an empty dictionary (implemented as hashmap in python)
        dicDoc={}
        key = ""
        writeInFile = False
        docBody = []
        #automatically closes after opening
        with open('cacm.all', 'r') as file:
            for line in file.readlines():
                #document ID '.I', title '.T', and abstract '.W' all occur before '.B'
                if ".B" in line:
                    writeInFile = False
                    #Store term frequencies
                    dictFreq = {}
                    for item in docBody:
                        dictFreq[item] = dictFreq.get(item,0)+1
                    #enumerate the body (Terms) and key is Document ID '.I'
                    dicDoc[key] = [list(enumerate(docBody)),dictFreq]
                    docBody = []
