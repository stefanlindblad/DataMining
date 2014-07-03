import numpy as np
import pandas
import newsfeatures as nf

# test of the functions implemented in newsfeatures.py


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


np.set_printoptions(threshold = np.nan)

# get all words in all feeds, all words in one feed each and all article themes
allwords, articlewords, articletitles = nf.getarticlewords(FEEDLIST)

# create the article-word-Matrix wordInArt
wordInArt, reasonableWords = nf.makematrix(allwords, articlewords)

# remove all articles with no important words in it.
wordInArt, articletitles = nf.removeallnullarticles(wordInArt, articletitles)

# compute featurematrix H and weightmatrix W with 5 features in 10 iterations
H, W = nf.nnmf(wordInArt, 5, 10)

# write article-word-matrix to .csv-file
wordInArtDataFrame = pandas.DataFrame(wordInArt, columns=reasonableWords)
wordInArtDataFrame.to_csv("wordInArt.csv")

# print features and article correlations. 
nf.showfeatures(W, H, articletitles, reasonableWords)
nf.showcorrelation(W, H, articletitles, reasonableWords)