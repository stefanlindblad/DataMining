import pylast as pyla
import experiment02.movies.recommendations as rec

network = pyla.get_lastfm_network()
artist = network.get_artist("Soulfly")
topfans = artist.get_top_fans(5)

fanNames = [a.item for a in topfans]
userDict = rec.createLastfmUserDict(fanNames)

print rec.topMatches(userDict, fanNames[0].name, rec.sim_euclid)

