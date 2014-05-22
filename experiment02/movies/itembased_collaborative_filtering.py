import recommendations as rec

transCritics = rec.transposeMatrix(rec.critics)

#2.4.1.2
similar_items_euclidean = rec.calculateSimilarItems(transCritics, rec.sim_euclid_normed)
similar_items_pearson = rec.calculateSimilarItems(transCritics, rec.sim_pearson)
print rec.topMatches(transCritics, 'Lady in the Water', rec.sim_euclid)

#2.4.1.3
print "Recommended Movies with euclidean: " + str(rec.getRecommendedItems(rec.critics, 'Toby Segaran', similar_items_euclidean))
print "Recommended Movies with pearson: " + str(rec.getRecommendedItems(rec.critics, 'Toby Segaran', similar_items_pearson))
