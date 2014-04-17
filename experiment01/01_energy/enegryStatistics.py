import pandas
from numpy import *
import matplotlib.pyplot as plt

energyInfo = pandas.read_csv('../resources/EnergyMix.csv')
print energyInfo.describe()

reducedEnergyInfo = energyInfo.drop("Total2009", 1)
reducedEnergyInfo = reducedEnergyInfo.drop("CO2Emm", 1)

plt.figure(1)
reducedEnergyInfo.boxplot()
plt.show()