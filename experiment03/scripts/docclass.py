def getwords(doc, minWordLength = 3, maxWordLength = 20):
    splittedStringList = doc.lower().split(" ")
    dict = {}
    for token in splittedStringList:
        if (len(token) > minWordLength and maxWordLength > len(token)):
            dict[token] = 1
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

    def incc(self, cat):
        self.cc[cat] += 1

    def fcount(self, f, cat):
        if(self.fc.has_key(f)):
            return self.fc[f][cat]
        else:
            return 0

    def catcount(self, cat):
        return self.cc[cat]

    def totalcount(self):
        return self.cc["Good"] + self.cc["Bad"]

    def train(self, item, cat):
        words = self.getfeatures(item)
        for w in words:
            self.incf(w, cat)
        self.incc(cat)

    def fprob(self,f,cat):
        return float(self.fcount(f, cat))/float(self.catcount(cat))

    def weightedprob(self, f, cat, initprob = 0.5):
        count = self.fcount(f, "Good") + self.fcount(f,"Bad")
        wprob = (initprob + count * self.fprob(f, cat))/(1 + count)
        return wprob









