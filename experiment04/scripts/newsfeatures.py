import feedparser
import re
import numpy as np
import pandas
from nltk.corpus import stopwords
import itertools as iter


# helper function to delete html/xml tags
def stripHTML(h):
  p=''
  s=0
  for c in h:
    if c=='<': s=1
    elif c=='>':
      s=0
      p+=' '
    elif s==0:
      p+=c
  return p


# helper function to traverse an iterable object from behind.
def reverse_enumerate(iterable):
    return iter.izip(reversed(xrange(len(iterable))), reversed(iterable))


# word separator helper function
sw=stopwords.words('english')
def separatewords(text):
    splitter=re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s) > 4 and s not in sw]


# function parses RSS feed entries, prints the articles and adds them to one big list parsedArticles
# feeds: list of feeds as strings
def parsefeeds(feeds):
    parsedArticles = []
    for feed in feeds:
        parsedFeed = feedparser.parse(feed)
        # print "--- News from " + feed + " ---"
        for e in parsedFeed.entries:
            # print "-" * 50
            fulltext=stripHTML(e.title+' '+e.description)
            # print fulltext
            parsedArticles.append({'title': stripHTML(e.title), 'description': stripHTML(e.description)})
       # print "-" * 50 + "\n"
    return parsedArticles


# function returns all words in all articles, all words in one article each and all article themes
# feeds: list of feeds as strings
def getarticlewords(feeds):
    articles = parsefeeds(feeds)
    allwords = {}
    articlewords = []
    articletitles = []

    for article in articles:
        articlewordlist = {}

        # create a string wholeArticle containing the title and the description of the article.
        wholeArticle = article["title"] + " " + article["description"]
        # get all the relevant words in wholeArticle
        splittedStringList = separatewords(wholeArticle.lower())

        for word in splittedStringList:
            # if allwords does not contain word add it to allwords with a default value of 1
            if not word in allwords:
                allwords[word] = 1
            # else the word is already in allwords and we can increment the value by 1
            else:
                allwords[word] += 1

            # if the word is not contained in articlewordlist, add an entry with a default value of 1
            if not word in articlewordlist:
                articlewordlist[word] = 1
            # else the word is already in articlewordlist and we can increment the value by 1/
            else:
                articlewordlist[word] += 1

        # add articlewordlist to articlewords
        articlewords.append(articlewordlist)
        # add the title of the article to articletitles.
        articletitles.append(article["title"])

    return allwords, articlewords, articletitles


# creates the article-word-matrix and
# a wordvector containing all reasonable words (more than 4 occurrences, appears in less than 60% of all articles).
# allwords: list of all words
# articlewords: list, that has a dictionary for each article, which maps the contained words to the occurrences of the word in the article.
def makematrix(allwords, articlewords):

    # get all words that occur 4 or more times.
    reasonableWords = [word for word in allwords if allwords[word] >= 4]

    # number of articles
    numarticles = len(articlewords)

    # check in how many articles the word occurs
    # if the word occurs in more than 60% of all articles, remove it from reasonableWords.
    appearances = 0
    for word in reasonableWords:
        for article in articlewords:
            if word in article:
                appearances += 1
        if (appearances / numarticles) > 0.6:
            reasonableWords.remove(word)

    # create the article-word-matrix and initialize with zeros
    wordInArt = np.zeros((len(articlewords), len(reasonableWords)))

    # for word i in reasonableWords...
    for i, word in enumerate(reasonableWords):
        # ... for article j
        for j, article in enumerate(articlewords):
            # if the article j contains the word i
            if word in (article):
                # add the number of occurrences of the word in the article at the matrix' position j,i
                wordInArt[j][i] = article[word]
    return wordInArt, reasonableWords


# Removes all articles that contain no reasonable words
# wordInArt: article-word-matrix
# articletitles: list of article titles
def removeallnullarticles(wordInArt, articletitles):
    # traverse the article from behind
    for index, article in reverse_enumerate(wordInArt):
        # check if the article has any entry greater than 0 for any word.
        articleHasWord = False
        for word in article:
             if word > 0:
                 articleHasWord = True
        # i f it doesnt delete the article from wordInArt and the according title from articletitles.
        if articleHasWord == False:
            wordInArt = np.delete(wordInArt, index, 0)
            articletitles.pop(index)

    return wordInArt, articletitles


# helper function to calculate the cost, i.e. the difference between two matrices
# Bsp:
#
#             A           B
#         | 0 1 2 |   | 1 2 3 |
# cost (  | 3 4 5 | , | 4 5 6 |  ) = (0-1)**2 + (1-2)**2 + ... + (8-9)**2 = 9
#         | 6 7 8 |   | 7 8 9 |
#
def cost(A, B):
    k = 0
    for i in xrange(0,len(A)):
        for j in xrange(0,len(A[i])):
            k += (A[i][j] - B[i][j])**2
    return k


# calculates the weightmatrix W and the featurematrix H
# from the Article-Word-Matrix A with m features and it iterations.
def nnmf(A, m, it):
    c = A.shape[1]      # number of words
    r = A.shape[0]      # number of articles
    H = np.random.random(m * c).reshape((m, c))
    W = np.random.random(r * m).reshape((r, m))

    for i in range(it):
        B = W.dot(H)
        # calculate the costs k
        k = cost(A,B)
        # check if the costs are lower than 5
        if(k <= 5):
            return (H, W)
        else:
            # calculate the new matrices
            H = np.array(H)*((np.array(W.T.dot(A)))/np.array(W.T.dot(W).dot(H)))
            W = np.array(W) *((np.array(A.dot(H.T)))/(np.array(W.dot(H).dot(H.T))))

    # return H and W if the costs are lower than 5 or the iteration process is over.
    return (H, W)


# extract the most important words for the feature at index i in descending order.
# h: featurematrix
# wordvec: list of all words
# i: index of feature
# quantity: number of words requested
def getimportantwords(h, wordvec, i, quantity = 6):
    wordlist = []
    for j,word in enumerate(wordvec):
        wordlist.append((h[i][j], wordvec[j]))
    return sorted(wordlist, reverse=True)[:quantity]


# task 2.3 from experiment 4
# w: weightmatrix
# : featurematrix
# titles: list of all articles
# wordvec: list of all words
# quantity: number of features requested
def getfeatures(w, h, titles, wordvec, quantity = 3):
    # printing most common features per article
    correlation = []
    for i,article in enumerate(w):
        featurelist = []
        for j,feature in enumerate(article):
            # get the 6 most important words for the feature at index j.
            importantWords = getimportantwords(h, wordvec, j)
            # strip the weight from the words, so that importantFeatures contains only the word itself.
            importantWords = [str(word[1]) for word in importantWords]
            featurelist.append((w[i][j], importantWords))
        # get the three most important features from featurelist
        articleFeatures = sorted(featurelist, reverse=True)[:quantity]
        correlation.append({'title': titles[i], 'features': articleFeatures})
    return correlation


# prints the article title and the most important features
# articles: list of articles
# quantity: amount of features to be printed.
def showfeatures(w, h, titles, wordvec, quantity = 3):
    articles = getfeatures(w, h, titles, wordvec, quantity)
    for article in articles:
        print article['title']
        print article['features'][:quantity]
        print '-' * 30


# will print a list of titles grouped by the most important feature
def getcorrelation(features):
    print "\n\n"
    print "=" * 50
    print '\nArticles and their 3 most important features:\n'
    print "=" * 50
    print "\n\n"

    highestFeatures = {}
    for article in features:
        # get the most important feature (at index 0) for the article
        # (we don't want the weight, too, so we just take the wordvector (at index 1) representing the feature)
        highestFeature = str(article['features'][0][1])
        # if there isn't an entry for this feature in highestFeatures, create it.
        if highestFeature not in highestFeatures:
            highestFeatures[highestFeature] = []
        # add the article title to the entry for the feature.
        highestFeatures[highestFeature].append(article['title'])
    return highestFeatures


# prints all features and for each feature a list of articles, for which the feature is the most important
def showcorrelation(w, h, titles, wordvec, quantity = 3):
    print "\n\n"
    print "=" * 50
    print '\nFeatures and articles for which the feature is the most important:\n'
    print "=" * 50
    print "\n\n"

    features = getfeatures(w, h, titles, wordvec, quantity = 3)
    correlation = getcorrelation(features)

    # for each feature in the correlation list...
    for key in correlation.keys():
        # print the 6 most important words in this feature
        print '\n\nall articles with feature: ' + key + ':\n'
        # print all titles, that have this feature as the most important.
        for title in correlation[key]:
            print title
        print '-' * 30
