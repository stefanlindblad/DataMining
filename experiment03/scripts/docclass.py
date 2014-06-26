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
        # if there is no word f in fc, create one with a category cat and a initial value of 0.
        if(not self.fc.has_key(f)):
            self.fc[f] = {cat:0}
        # if the word f has no category cat, create it and initialize it with 0.
        if(not self.fc[f].has_key(cat)):
            self.fc[f][cat] = 0
        # add 1 to the corresponding category in the entry of word f.
        self.fc[f][cat] += 1

    def incc(self, cat):
        # if there is no category cat in cc, create on and initialize it with 0.
        if(not self.cc.has_key(cat)):
            self.cc[cat] = 0
        # add 1 to the category.
        self.cc[cat] += 1

    def fcount(self, f, cat):
        # check if the word f is contained in fc.
        if(self.fc.has_key(f)):
            # check if the entry of word f contains the category cat
            if(self.fc[f].has_key(cat)):
                # return the corresponding value of the word f for the category cat.
                return self.fc[f][cat]
                # else return 0.
            else:
                return 0
        else:
            return 0

    def catcount(self, cat):
        #return the total number of documents for the category cat.
        return self.cc[cat]

    def totalcount(self):
        totalcount = 0
        # add all documents in each category to totalcount.
        for cat in self.cc.iterkeys():
            totalcount += self.cc[cat]
        # return totalcount.
        return totalcount

    def train(self, item, cat):
        # for the document item get all words as a dict.
        words = self.getfeatures(item)

        # for each word in words...
        for w in words:
            # ... add 1 to the entry of the word in fc for the category cat.
            self.incf(w, cat)
        # add one to the amount of documents in the category cat.
        self.incc(cat)

    def fprob(self,f,cat):
        # return the probability, that the word f is contained in documents of the category cat,
        # by dividing the amount of documents in the category cat, that contain the word f,
        # by the total amount of documents in the category cat.
        return float(self.fcount(f, cat))/float(self.catcount(cat))

    def weightedprob(self, f, cat):
        # count is the number of appearances of the word f in all documents of all categories.
        count = 0
        for category in self.cc.iterkeys():
            x = self.fcount(f, category)
            count += x

        # the more often the word appears in the documents the smaller is the influence of initprob.
        wprob = (self.initprob + count * self.fprob(f, cat))/(1 + count)
        return wprob

    def prob(self, item, cat):
        words = self.getfeatures(item)
        allProbs = 1
        # the variable allProbs is the product of the probability of every word contained in the document item.
        for w in words:
            allProbs *= float(self.weightedprob(w, cat))
        # the variable probCat is the probability, that a document is classified for category cat. It is determined
        # by deviding the amount of documents in the category cat by the total amount of documents.
        probCat = float(self.catcount(cat))/float(self.totalcount())

        return allProbs * probCat

    def classify(self, item):
        # cats is a dictionary that assigns each category a probability, that the document item is in this category.
        cats = {}
        # each category is added to cats and the probability is assigned
        for cat in self.cc.iterkeys():
            cats[cat] = self.prob(item, cat)

        # the highest probability is determined and returned. 
        key = None
        val = 0
        for cat in cats.iterkeys():
            if cats[cat] > val:
                key = cat
                val = cats[cat]
        return key








