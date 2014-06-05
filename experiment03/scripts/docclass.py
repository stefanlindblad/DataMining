def getwords(doc, minWordLength = 3, maxWordLength = 20):
    splittedStringList = doc.lower().split(" ")
    dict = {}
    for token in splittedStringList:
        if (len(token) > minWordLength and maxWordLength > len(token)):
            dict[token] = 1
    print dict
    return dict

class Classifier():

    def __init__(self, featureFunction):
        self.fc = {}
        self.cc = {"Bad" : 0, "Good" : 0}
        self.getfeatures = featureFunction

    def incf(self, f, cat):
        if(not self.fc.has_key(f)):
            self.fc[f] = {"Good":0, "Bad":0}
        self.fc[f][cat] += 1

    def incc(self,cat):
        self.cc[cat] += 1

    def fcount(self,f,cat):
        if(self.fc.has_key(f)):
            return self.fc[f][cat]
        else:
            return 0

    def catcount(self,cat):
        return self.cc[cat]

    def totalcount(self):
        return self.cc["Good"] + self.cc["Bad"]








