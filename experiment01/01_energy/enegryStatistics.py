import pandas
import matplotlib.pyplot as plt

ENERGYFORMS = ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']
NUM_ENERGYFORMS = len(ENERGYFORMS)

energyInfo = pandas.read_csv('../resources/EnergyMixGeo.csv')
print energyInfo.describe()

reducedEnergyInfo = energyInfo[ENERGYFORMS]

plt.figure(1)
plt.boxplot(reducedEnergyInfo.values, sym='')
plt.show()