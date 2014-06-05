def getwords(self, doc, minWordLength = 3, maxWordLength = 20):
    splittedStringList = doc.lower().split(" ")
    dict = {}
    for token in splittedStringList:
        if (len(token) > minWordLength and maxWordLength > len(token)):
            dict[token] = 1
    print dict
    return dict

class Classifier():
    getfeatures = getwords
    
    def __init__(self):
        self.fc = {}
        self.cc = {"Bad" : 0, "Good" : 0}






