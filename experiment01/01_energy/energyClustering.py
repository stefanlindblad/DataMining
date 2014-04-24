import pandas
from pylab import find
from scipy import spatial, cluster
from sklearn import preprocessing
from numpy import *
import matplotlib.pyplot as plt

NUM_CLUSTER = 4
ENERGYFORMS = ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']
NUM_ENEGRYFORMS = len(ENERGYFORMS)

energyInfo = pandas.read_csv('../resources/EnergyMixGeo.csv')
reducedEnergyInfo = energyInfo[ENERGYFORMS]

preprocessedEnergyInfo = preprocessing.scale(reducedEnergyInfo, with_mean = False)

relativeEnergyConsumption = spatial.distance.pdist(preprocessedEnergyInfo, metric = 'correlation')

linkageMatrix = cluster.hierarchy.linkage(relativeEnergyConsumption, method='average')
cluster.hierarchy.dendrogram(linkageMatrix, orientation = 'left', labels = energyInfo.Country.values)

coutryToClusterLinkage = cluster.hierarchy.fcluster(linkageMatrix, NUM_CLUSTER, criterion='maxclust')
coutryToClusterLinkage -= 1

plt.figure(1)
for clusterIndex in range(NUM_CLUSTER):
    print '-'*10 + 'Cluster ' + str(clusterIndex) + '-'*10
    ind=find(coutryToClusterLinkage==clusterIndex)
    for a in ind:
        print energyInfo.Country.values[a]

sum = zeros((NUM_CLUSTER, NUM_ENEGRYFORMS))

plt.figure(2)
for countryIndex, clusterIndex in enumerate(coutryToClusterLinkage):
    plt.subplot(NUM_CLUSTER, 1, clusterIndex + 1)
    plt.plot(reducedEnergyInfo.values[countryIndex,:])
    plt.title('Cluster ' + str(clusterIndex))
    plt.xticks(range(NUM_ENEGRYFORMS), reducedEnergyInfo.columns.values)
    for energyIndex in range(NUM_ENEGRYFORMS):
        sum[clusterIndex, energyIndex] += reducedEnergyInfo.values[countryIndex,energyIndex]

plt.figure(3)
for clusterIndex in range(NUM_CLUSTER):
    plt.subplot(NUM_CLUSTER, 1, clusterIndex + 1)
    plt.plot(sum[clusterIndex, :])
    plt.title('Cluster ' + str(clusterIndex))
    plt.xticks(range(NUM_ENEGRYFORMS), reducedEnergyInfo.columns.values)

plt.show()

energyInfo['clusterIndex'] = pandas.Series(coutryToClusterLinkage)

energyInfo.to_csv('EnegryMixGeo.csv');