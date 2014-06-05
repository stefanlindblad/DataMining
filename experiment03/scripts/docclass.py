def getwords(doc, minWordLength = 3, maxWordLength = 20):
    splittedStringList = doc.lower().split(" ")
    dict = {}
    for token in splittedStringList:
        if (len(token) > minWordLength and maxWordLength > len(token)):
            dict[token] = 1
    return dict

class Classifier():

    def __init__(self, featureFunction, a = "Good", b = "Bad",initprob = 0.5):
        self.initprob = initprob
        self.cat1 = a
        self.cat2 = b
        self.fc = {}
        self.cc = {b : 0, a : 0}
        self.getfeatures = featureFunction

    def incf(self, f, cat):
        if(not self.fc.has_key(f)):
            self.fc[f] = {self.cat1:0, self.cat2:0}
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
        return self.cc[self.cat1] + self.cc[self.cat2]

    def train(self, item, cat):
        words = self.getfeatures(item)
        for w in words:
            self.incf(w, cat)
        self.incc(cat)

    def fprob(self,f,cat):
        return float(self.fcount(f, cat))/float(self.catcount(cat))

    def weightedprob(self, f, cat):
        count = self.fcount(f, self.cat1) + self.fcount(f,self.cat2)
        wprob = (self.initprob + count * self.fprob(f, cat))/(1 + count)
        return wprob

    def prob(self, item, cat):
        words = self.getfeatures(item)
        allProbs = 1.0
        for w in words:
            allProbs *= float(self.weightedprob(w, cat))
        probCat = float(self.catcount(cat))/float(self.totalcount())
        return allProbs * probCat

    def classify(self, item):
        good = self.prob(item, self.cat1)
        bad = self.prob(item, self.cat2)

        return self.cat1 if (good >= bad) else self.cat2








