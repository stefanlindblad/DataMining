import feedparser
import re
import numpy as np
import pandas
from nltk.corpus import stopwords
import itertools as iter

FEEDLIST = ['http://feeds.reuters.com/reuters/topNews',
            'http://feeds.reuters.com/reuters/businessNews',
            'http://feeds.reuters.com/reuters/worldNews',
            'http://feeds2.feedburner.com/time/world',
            'http://feeds2.feedburner.com/time/business',
            'http://feeds2.feedburner.com/time/politics',
            'http://rss.cnn.com/rss/edition.rss',
            'http://rss.cnn.com/rss/edition_world.rss',
            'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/rss.xml',
            'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/europe/rss.xml',
            'http://rss.nytimes.com/services/xml/rss/nyt/World.xml',
            'http://rss.nytimes.com/services/xml/rss/nyt/Economy.xml']

# deletes html / xml tags
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

def reverse_enumerate(iterable):
    return iter.izip(reversed(xrange(len(iterable))), reversed(iterable))

# word separator helper function
sw=stopwords.words('english')
def separatewords(text):
    splitter=re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s) > 4 and s not in sw]

# function parses RSS feed entries, prints them and adds them to one big list
def parsefeeds(feeds):
    parsedFeeds = []
    for feed in feeds:
        parsedFeed = feedparser.parse(feed)
        # print "--- News from " + feed + " ---"
        for e in parsedFeed.entries:
            # print "-" * 50
            fulltext=stripHTML(e.title+' '+e.description)
            # print fulltext
            parsedFeeds.append({'title': stripHTML(e.title), 'description': stripHTML(e.description)})
       # print "-" * 50 + "\n"
    return  parsedFeeds



# function returns all words in all feeds, all words in one feed each and all article themes
def getarticlewords():
    feeds = parsefeeds(FEEDLIST)
    allwords = {}
    articlewords = []
    articletitles = []

    splittedStringList = ""
    for feed in feeds:
        articlewordlist = {}
        wholeFeed = feed["title"] + " " + feed["description"]
        splittedStringList = separatewords(wholeFeed.lower())
        for word in splittedStringList:

            if not word in allwords:
                allwords[word] = 1
            else:
                allwords[word] += 1

            if not word in articlewordlist:
                articlewordlist[word] = 1
            else:
                articlewordlist[word] += 1

        articlewords.append(articlewordlist)
        articletitles.append(feed["title"])

    return allwords, articlewords, articletitles

# functions makes a matrix!
def makematrix(allwords, articlewords):
    reasonableWords = [word for word in allwords if allwords[word] >= 4]

    articles = len(articlewords)
    wordAppearsInArticle = 0
    for word in reasonableWords:
        for article in articlewords:
            if word in article:
                wordAppearsInArticle += 1

        if (wordAppearsInArticle / articles) > 0.6:
            reasonableWords.remove(word)

    wordInArtArray = np.zeros((len(articlewords), len(reasonableWords)));
    for i, word in enumerate(reasonableWords):
        for j, article in enumerate(articlewords):
            if word in (article):
                wordInArtArray[j][i] = article[word]

    return reasonableWords, wordInArtArray

#Removes all articles that contain no reasonable words
def removeallnullarticles(wordInArt, articletitles):
    for index, article in reverse_enumerate(wordInArt):
        articleHasWord = False
        for word in article:
             if word > 0:
                 articleHasWord = True

        if articleHasWord == False:
            wordInArt = np.delete(wordInArt, index, 0)
            articletitles.pop(index)

    return wordInArt, articletitles


def gethighestfeatures(matrix, wordvec, i, feature, count):
    wordlist = []
    for j,word in enumerate(wordvec):
        wordlist.append((matrix[i][j], wordvec[j]))
    return sorted(wordlist, reverse=True)[:count]

# task 2.3 from experiment 4
# weightmatrix w
# featurematrix h
# list of all articles: titles
# list of all words: wordvec
def getfeatures(w, h, titles, wordvec):
    # printing most common features per article
    correlation = []
    for i,article in enumerate(w):
        featurelist = []
        for j,feature in enumerate(article):
            wichtigsteMerkmale = gethighestfeatures(h, wordvec, j, feature, 6)
            wichtigsteMerkmale = [str(merkmal[1]) for merkmal in wichtigsteMerkmale]
            featurelist.append((w[i][j], wichtigsteMerkmale))
        articleFeatures = sorted(featurelist, reverse=True)[:3]
        correlation.append({'title': titles[i], 'features': articleFeatures})
    return correlation

def showfeatures(features):
    for article in features:
        print article['title']
        print article['features'][:3]
        print '-' * 30

# will print a list of titles grouped by the most important feature
# weightmatrix w
# featurematrix h
# list of all articles: titles
# list of all words: wordvec
def getcorrelation(features):
    highestFeatures = {}
    for article in features:
        highestFeature = str(article['features'][0][1])
        if highestFeature not in highestFeatures:
            highestFeatures[highestFeature] = []
        highestFeatures[highestFeature].append(article['title'])
    return highestFeatures

def showcorrelation(correlation):
    for key in correlation.keys():
        print 'all articles with feature: ' + key + ':'
        for title in correlation[key]:
            print title
        print '-' * 30

def cost(A, B):
    k = 0
    for i in xrange(0,len(A)):
        for j in xrange(0,len(A[i])):
            k += (A[i][j] - B[i][j])**2
    return k


def nnmf(A, m, it):
    c = A.shape[1]      # number of words
    r = A.shape[0]      # number of articles
    H = np.random.random(m * c).reshape((m, c))
    W = np.random.random(r * m).reshape((r, m))

    for i in range(it):
        B = W.dot(H)
        k = cost(A,B)
        if(k <= 5):

            return (H, W)
        else:
            H = np.array(H)*((np.array(W.T.dot(A)))/np.array(W.T.dot(W).dot(H)))
            W = np.array(W) *((np.array(A.dot(H.T)))/(np.array(W.dot(H).dot(H.T))))



    return (H, W)


# execution
np.set_printoptions(threshold = np.nan)
allwords, articlewords, articletitles = getarticlewords()
reasonableWords, wordInArt = makematrix(allwords, articlewords)

wordInArt, articletitles = removeallnullarticles(wordInArt, articletitles)

print(wordInArt)
H, W = nnmf(wordInArt, 5, 5)

wordInArtDataFrame = pandas.DataFrame(wordInArt, columns=reasonableWords)
wordInArtDataFrame.to_csv("wordInArt.csv")

features = getfeatures(W, H, articletitles, reasonableWords)
correlation = getcorrelation(features)

showfeatures(features)
showcorrelation(correlation)
