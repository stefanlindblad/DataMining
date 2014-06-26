import feedparser
import numpy as np

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

def parseFeeds(feeds):
    parsedFeeds = []
    for feed in feeds:
        parsedFeed = feedparser.parse(feed)
        print "--- News from " + feed + " ---"
        for e in parsedFeed.entries:
            print "-" * 50
            fulltext=stripHTML(e.title+' '+e.description)
            print fulltext
            parsedFeeds.append((e.title, e.description))
        print "-" * 50 + "\n"
    return  parsedFeeds


# parseFeeds(FEEDLIST)


def cost(A, B):
    c = 0
    for i in xrange(0,len(A)):
        for j in xrange(0,len(A[i])):
            c += (A[i][j] - B[i][j])**2
    return c
