import recommendations as rec

# for person in rec.critics:
    # print ("Euklid Top Match: \t" + person + "\t" + str(rec.topMatches(rec.critics, person, rec.sim_euclid)[0]))
    # print ("Pearson Top Match: \t" + person + "\t" + str(rec.topMatches(rec.critics, person, rec.sim_pearson)[0]))

print rec.getRecommendations(rec.critics, 'Toby Segaran', rec.sim_pearson)

