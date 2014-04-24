import pandas
from pylab import find
from scipy import spatial, cluster
from sklearn import preprocessing
from numpy import *
import matplotlib.pyplot as plt

NUM_CLUSTER = 4

energyInfo = pandas.read_csv('../resources/EnergyMix.csv')
reducedEnergyInfo = energyInfo.drop("Country", 1)
reducedEnergyInfo = reducedEnergyInfo.drop("Total2009", 1)
reducedEnergyInfo = reducedEnergyInfo.drop("CO2Emm", 1)

preprocessedEnergyInfo = preprocessing.scale(reducedEnergyInfo, with_mean = False)

relativeEnergyConsumption = spatial.distance.pdist(preprocessedEnergyInfo, metric = 'correlation')

linkageMatrix = cluster.hierarchy.linkage(relativeEnergyConsumption)
cluster.hierarchy.dendrogram(linkageMatrix, orientation = 'left', labels = energyInfo.Country.values)

clustlabels = cluster.hierarchy.fcluster(linkageMatrix, NUM_CLUSTER, criterion='maxclust')
clustlabels -= 1

plt.figure(1)
for cl in range(NUM_CLUSTER):
    print '-'*10 + 'Cluster ' + str(cl) + '-'*10
    ind=find(clustlabels==cl)
    for a in ind:
        print energyInfo.Country.values[a]

plt.figure(2)


for index, cl in enumerate(clustlabels):
    plt.subplot(NUM_CLUSTER, 1, cl)
    plt.plot(reducedEnergyInfo.values[index,:])

for cl in range(NUM_CLUSTER):
    plt.subplot(NUM_CLUSTER, 1, cl)
    plt.title('Cluster ' + str(cl))
    plt.xticks(range(5), reducedEnergyInfo.columns.values)



plt.show()



