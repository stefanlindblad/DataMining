# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby Segaran': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

from math import sqrt
import numpy as np
import operator

def sim_euclid_normed(prefs, person1, person2):
    return sim_euclid(prefs, person1, person2, True)


def sim_euclid(prefs,person1,person2,normed=False):
  ''' Returns a euclidean-distance-based similarity score for 
  person1 and person2. In the distance calculation the sum is computed 
  only over those items, which are nonzero for both instances, i.e. only
  films which are ranked by both persons are regarded.
  If the parameter normed is True, then the euclidean distance is divided by
  the number of non-zero elements integrated in the distance calculation. Thus
  the effect of larger distances in the case of an increasing number of commonly ranked
  items is avoided.
  '''
  # Get the list of shared_items
  si={}
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1
  # len(si) counts the number of common ratings
  # if they have no ratings in common, return 0
  if len(si)==0: return 0

  # Add up the squares of all the differences
  sum_of_squares=sqrt(sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                     for item in prefs[person1] if item in prefs[person2]]))
  if normed:
     sum_of_squares= 1.0/len(si)*sum_of_squares
  return 1/(1+sum_of_squares)


def sim_pearson(prefs,p1,p2):
  '''
  Returns the Pearson correlation coefficient for p1 and p2
  '''
    
  # Get the list of commonly rated items
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1

  # if they are no ratings in common, return 0
  if len(si)==0: return 0

  # Sum calculations
  n=len(si)
  
  # Calculate means of person 1 and 2
  mp1=np.mean([prefs[p1][it] for it in si])
  mp2=np.mean([prefs[p2][it] for it in si])
  
  # Calculate standard deviation of person 1 and 2
  sp1=np.std([prefs[p1][it] for it in si])
  sp2=np.std([prefs[p2][it] for it in si])
  
  # If all elements in one sample are identical, the standard deviation is 0. 
  # In this case there is no linear correlation between the samples
  if sp1==0 or sp2==0:
      return 0
  r=1/(n*sp1*sp2)*sum([(prefs[p1][it]-mp1)*(prefs[p2][it]-mp2) for it in si])
  return r


def sim_RusselRao(prefs,person1,person2,normed=True):
  ''' Returns RusselRao similaritiy between 2 users. The RusselRao similarity just counts the number
  of common non-zero components of the two vectors and divides this number by N, where N is the length
  of the vectors. If normed=False, the division by N is omitted.
  '''
  # Get the list of shared_items
  si={}
  commons=0
  for item in prefs[person1]: 
    if prefs[person1][item]==1 and prefs[person2][item]==1:   
        commons+=1
  #print commons
  if not normed:
      return commons
  else:
      return commons*1.0/len(prefs[person1])  
      

def topMatches(prefs, person, similarity):

    sim = {}
    for candidate in prefs:
        if candidate == person:
            continue
        sim[candidate] = similarity(prefs, person, candidate)

    return sorted(sim.iteritems(), key=operator.itemgetter(1), reverse=True)

def getRecommendations(prefs, person, similarity):

    # compute correlations 
    sim = {}
    for candidate in prefs:
        if candidate == person:
            continue
        sim[candidate] = similarity(prefs, person, candidate)

    kSums = {}
    unknownMedia = {}
    for candidate in prefs:
        # don't compare a person with itself
        if candidate == person:
            continue
        # if the correlation is negative the persons are too different.
        if sim[candidate] < 0:
            continue
        # for every media the candidate already knows
        for media in prefs[candidate]:
            # ... check if the person doesn't know it, too.
            if media not in prefs[person] or prefs[person][media] == 0:
                # check if the not yet seen media is already in the unknownMedia list.
                # if not add it to unknownMedia and kSums with value 0
                if media not in unknownMedia:
                    unknownMedia[media] = 0
                    kSums[media] = 0
                # add the correlation of the candidate to the kSum of the current media.
                kSums[media] += sim[candidate]
                # add the recommendation of the candidate times the correlation to the sum of the current media
                unknownMedia[media] += sim[candidate] * prefs[candidate][media]

    # divide the sum of the media by the kSum of the media
    for media in unknownMedia:
        unknownMedia[media] = unknownMedia[media]/kSums[media]

    # switch keys and values in the dictionary to get tuples of (recommendation , name) instead of (name , recommendation) later
    # unknownMedia = {y:x for x,y in unknownMedia.iteritems()}

    # sort dictionary into list by descending keys (recommendation score)
    list = sorted(unknownMedia.iteritems(), key=lambda t: t[1], reverse=True)

    return list


def createLastfmUserDict(userNames):

    NUMBER_OF_BANDS = 20
    allBands = {}
    userDict = {}

    # adding all bands from the users to the allBand dictionary
    for user in userNames:
        topBands = user.get_top_artists()[0:NUMBER_OF_BANDS]
        for band in topBands:
            allBands[str(band.item)] = 0 #item is the name

    # creating the dictionary with 0/1 bands for every user
    for user in userNames:
        topBands = user.get_top_artists()[0:NUMBER_OF_BANDS]
        userDict[str(user)] = allBands.copy()
        for band in allBands:
            for topBand in topBands:
                if str(band) == str(topBand.item):
                    userDict[str(user)][band] = 1

    return userDict


def topMatches(prefs, person, similarity):

    sim = {}
    list = []
    for candidate in prefs:
        if candidate == person:
            continue
        sim[candidate] = similarity(prefs, person, candidate)

    return sorted(sim.iteritems(), key=operator.itemgetter(1), reverse=True)

def getAllProducts(prefs):
    products = []
    for person in prefs:
        for product in prefs[person]:
            if product not in products: products.append(product)
    return products


def transposeMatrix(prefs):
    products = getAllProducts(prefs)
    transCritics = {}
    for product in products:
        for person in prefs:
            if product in prefs[person]:
                if product not in transCritics:
                    transCritics[product] = {}
                transCritics[product][person] = prefs[person][product]
    return transCritics


def calculateSimilarItems(prefs, similarity):
    '''
    processes similarity between all movies and returns a dictionary.
    '''
    similarity_matrix = {}
    for pref in prefs: similarity_matrix[pref] = dict(topMatches(prefs, pref, similarity))
    return similarity_matrix


def getRecommendedItems(prefs, name, similar_items):
    rated_items = prefs[name]
    unrated_items = []
    recommendations = {}
    transCritics = transposeMatrix(prefs)

    # save unrated items in new list unrated_items
    for item in transCritics:
        if item not in rated_items: unrated_items.append(item)

    for unrated_item in unrated_items:
        sum_similarity = 0.0
        item_rated_similarity = 0.0
        for rated_item in rated_items:
            similarity = similar_items[rated_item][unrated_item]
            if similarity > 0.0:
                sum_similarity += similarity
                item_rated_similarity += similarity * prefs[name][rated_item]
        if sum_similarity > 0.0:
            recommendations[unrated_item] = item_rated_similarity / sum_similarity
    return sorted(recommendations.iteritems(), key=operator.itemgetter(1), reverse=True)