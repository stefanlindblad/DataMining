def getwords(doc, minWordLength = 3, maxWordLength = 20):
    splittedStringList = doc.lower().split(" ")
    dict = {}
    for token in splittedStringList:
        if (len(token) > minWordLength and maxWordLength > len(token)):
            dict[token] = 1
    return dict

class Classifier():

    def __init__(self, featureFunction, initprob = 0.5):
        self.initprob = initprob
        self.fc = {}
        self.cc = {}
        self.getfeatures = featureFunction

    def incf(self, f, cat):
        if(not self.fc.has_key(f)):
            self.fc[f] = {cat:0}
        if(not self.fc[f].has_key(cat)):
            self.fc[f][cat] = 0
        self.fc[f][cat] += 1

    def incc(self, cat):
        if(not self.cc.has_key(cat)):
            self.cc[cat] = 0
        self.cc[cat] += 1

    def fcount(self, f, cat):
        if(self.fc.has_key(f)):
            if(self.fc[f].has_key(cat)):
                return self.fc[f][cat]
            else:
                return 0
        else:
            return 0

    def catcount(self, cat):
        return self.cc[cat]

    def totalcount(self):
        totalcount = 0
        for cat in self.cc.iterkeys():
            totalcount += self.cc[cat]
        return totalcount

    def train(self, item, cat):
        words = self.getfeatures(item)
        for w in words:
            self.incf(w, cat)
        self.incc(cat)

    def fprob(self,f,cat):
        return float(self.fcount(f, cat))/float(self.catcount(cat))

    def weightedprob(self, f, cat):
        count = 0
        for category in self.cc.iterkeys():
            x = self.fcount(f, category)
            count += x

        wprob = (self.initprob + count * self.fprob(f, cat))/(1 + count)
        return wprob

    def prob(self, item, cat):
        words = self.getfeatures(item)
        allProbs = 1
        for w in words:
            allProbs *= float(self.weightedprob(w, cat))
        probCat = float(self.catcount(cat))/float(self.totalcount())
        return allProbs * probCat

    def classify(self, item):
        cats = {}
        for cat in self.cc.iterkeys():
            cats[cat] = self.prob(item, cat)
        key = None
        val = 0
        for cat in cats.iterkeys():
            if cats[cat] > val:
                key = cat
                val = cats[cat]
        return key








