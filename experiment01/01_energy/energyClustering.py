import pandas
from pylab import find
from scipy import spatial, cluster
from sklearn import preprocessing
from numpy import *
import matplotlib.pyplot as plt

energyInfo = pandas.read_csv('../resources/EnergyMix.csv')
reducedEnergyInfo = energyInfo.drop("Country", 1)
reducedEnergyInfo = reducedEnergyInfo.drop("Total2009", 1)
reducedEnergyInfo = reducedEnergyInfo.drop("CO2Emm", 1)

preprocessedEnergyInfo = preprocessing.scale(reducedEnergyInfo, with_mean = False)

relativeEnergyConsumption = spatial.distance.pdist(preprocessedEnergyInfo, metric = 'correlation')

linkageMatrix = cluster.hierarchy.linkage(relativeEnergyConsumption)
cluster.hierarchy.dendrogram(linkageMatrix, orientation = 'left', labels = energyInfo.Country.values)

clustlabels = cluster.hierarchy.fcluster(linkageMatrix, 4, criterion='maxclust')
clustlabels -= 1

for cl in range(4):
    print '-'*10 + 'Cluster ' + str(cl) + '-'*10
    ind=find(clustlabels==cl)
    for a in ind:
        print energyInfo.Country.values[a]

plt.show()