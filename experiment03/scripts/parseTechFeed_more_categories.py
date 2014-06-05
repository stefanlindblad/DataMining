import feedparser
from docclass import Classifier
from docclass import getwords


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

# trainNonTechOriginal=['http://newsfeed.zeit.de/index',
#               'http://newsfeed.zeit.de/wirtschaft/index',
#               'http://www.welt.de/politik/?service=Rss',
#               'http://www.spiegel.de/schlagzeilen/tops/index.rss',
#               'http://www.sueddeutsche.de/app/service/rss/alles/rss.xml'
#               ]

#Technik
trainTech=['http://rss.chip.de/c/573/f/7439/index.rss',
           'http://rss.chip.de/c/573/f/7455/index.rss',
           'http://golem.de.dynamic.feedsportal.com/pf/578068/http://rss.golem.de/rss.php?r=hw&feed=RSS2.0',
           'http://rss.chip.de/c/573/f/7440/index.rss',
           'http://www.computerbild.de/rssfeed_2261.html?node=10',
           'http://www.computerbild.de/rssfeed_2261.xml?node=13']

#Politics
trainPolitics = ['http://www.spiegel.de/politik/index.rss',
                 'http://www.welt.de/politik/?service=Rss',
                 'http://politropolis.wordpress.com/feed/',
                 'http://www.tagesspiegel.de/contentexport/feed/politik',
                 'http://www.faz.net/rss/aktuell/politik/',
                 'http://www.lehrer-online.de/rss-materialien-politik-sowi.xml',
                 'http://rss.sueddeutsche.de/rss/Politik']

#Wirtschaftsfeeds
trainEconomy=['http://www.manager-magazin.de/finanzen/index.rss',
              'http://newsfeed.zeit.de/wirtschaft/index',
              'http://www.handelsblatt.com/contentexport/feed/finanzen',
              'http://www.handelsblatt.com/contentexport/feed/wirtschaft',
              'http://www.wiwo.de/contentexport/feed/rss/finanzen',
              'http://www.faz.net/rss/aktuell/wirtschaft/konjunktur/',
              'http://www.faz.net/rss/aktuell/wirtschaft/eurokrise/']

#Sport
trainSport = ['http://sportbild.bild.de/services/rss/sportbild-alle-artikel-10185954,sort=1,n=25,view=rss2.sport.xml',
              'http://www.welt.de/sport/?service=Rss',
              'http://feeds.t-online.de/rss/sport',
              'http://rss.kicker.de/news/aktuell',
              'http://www.faz.net/rss/aktuell/sport/fussball/',
              'http://www.faz.net/rss/aktuell/sport/mehr-sport/',
              'http://rss.sueddeutsche.de/rss/Sport']

trainScience = ['http://www.wissenschaft-aktuell.de/onTEAM/WSA-Natur.xml',
                'http://www.wissenschaft-aktuell.de/onTEAM/WSA-Mensch.xml',
                'http://www.scienceticker.info/feed/',
                'http://www.weltderphysik.de/intern/index.php?PID=34',
                'http://www.faz.net/rss/aktuell/wissen/medizin/',
                'http://www.faz.net/rss/aktuell/wissen/weltraum/',
                'http://img.geo.de/rss/GEO/index.xml']

test=["http://suche.sueddeutsche.de/?output=rss",
          'http://newsfeed.zeit.de/politik/index',  
          'http://www.welt.de/?service=Rss',
          'http://www.haz.de/rss/feed/haz_schlagzeilen']



countnews={}
countnews['tech']=0
countnews['sports']=0
countnews['economy']=0
countnews['politics']=0
countnews['science']=0

countnews['test']=0


c = Classifier(getwords, initprob=0.5)

print "--------------------News from trainTech------------------------"
for feed in trainTech:
    f=feedparser.parse(feed)
    for e in f.entries:
        print '\n---------------------------'
        fulltext=stripHTML(e.title+' '+e.description)
        print fulltext
        countnews['tech']+=1

        c.train(fulltext,"Tech")

print "----------------------------------------------------------------"
print "----------------------------------------------------------------"
print "----------------------------------------------------------------"

print "--------------------News from trainPolitics------------------------"
for feed in trainPolitics:
    f=feedparser.parse(feed)
    for e in f.entries:
        print '\n---------------------------'
        fulltext=stripHTML(e.title+' '+e.description)
        print fulltext
        countnews['politics']+=1
        c.train(fulltext, "Politics")

print "----------------------------------------------------------------"
print "----------------------------------------------------------------"
print "----------------------------------------------------------------"

print "--------------------News from trainEconomy------------------------"
for feed in trainEconomy:
    f=feedparser.parse(feed)
    for e in f.entries:
        print '\n---------------------------'
        fulltext=stripHTML(e.title+' '+e.description)
        print fulltext
        countnews['economy']+=1
        c.train(fulltext, "Economy")

print "----------------------------------------------------------------"
print "----------------------------------------------------------------"
print "----------------------------------------------------------------"

print "--------------------News from trainScience------------------------"
for feed in trainScience:
    f=feedparser.parse(feed)
    for e in f.entries:
        print '\n---------------------------'
        fulltext=stripHTML(e.title+' '+e.description)
        print fulltext
        countnews['science']+=1
        c.train(fulltext, "Science")

print "----------------------------------------------------------------"
print "----------------------------------------------------------------"
print "----------------------------------------------------------------"

print "--------------------News from trainSport------------------------"
for feed in trainSport:
    f=feedparser.parse(feed)
    for e in f.entries:
        print '\n---------------------------'
        fulltext=stripHTML(e.title+' '+e.description)
        print fulltext
        countnews['sports']+=1
        c.train(fulltext, "Sports")

print "----------------------------------------------------------------"
print "----------------------------------------------------------------"
print "----------------------------------------------------------------"

print "--------------------News from test------------------------"
for feed in test:
    f=feedparser.parse(feed)
    for e in f.entries:
        print '\n---------------------------'
        fulltext=stripHTML(e.title+' '+e.description)
        print fulltext
        countnews['test']+=1

        print "Klassifikation: " + c.classify(fulltext)

print "----------------------------------------------------------------"
print "----------------------------------------------------------------"
print "----------------------------------------------------------------"



print 'Number of used trainings samples in categorie tech',countnews['tech']
print 'Number of used trainings samples in categorie sports',countnews['sports']
print 'Number of used trainings samples in categorie economy',countnews['economy']
print 'Number of used trainings samples in categorie politics',countnews['politics']
print 'Number of used trainings samples in categorie science',countnews['science']
print 'Number of used test samples',countnews['test']
print '--'*30




