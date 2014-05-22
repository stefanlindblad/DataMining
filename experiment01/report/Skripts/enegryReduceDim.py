import pandas
from sklearn import manifold
import matplotlib.pyplot as plt

ENERGYFORMS = ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']
NUM_ENERGYFORMS = len(ENERGYFORMS)

energyInfo = pandas.read_csv('../resources/EnergyMixGeo.csv')
reducedEnergyInfo = energyInfo[ENERGYFORMS]

isomap = manifold.Isomap(n_neighbors=NUM_ENERGYFORMS, n_components=2, eigen_solver='auto')

transformedEnergyInfo = isomap.fit_transform(reducedEnergyInfo)

plt.figure()

plt.scatter(transformedEnergyInfo[:, 0], transformedEnergyInfo[:, 1])

for index, country in enumerate(energyInfo.Country):
    plt.annotate(
        country,
        xy = (transformedEnergyInfo[index, 0], transformedEnergyInfo[index, 1]), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.show()