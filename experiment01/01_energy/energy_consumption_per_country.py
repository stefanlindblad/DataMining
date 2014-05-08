
import pandas
from numpy import *
import matplotlib.pyplot as plt


energy = pandas.read_csv('../resources/EnergyMix.csv')


print energy[list(energy.columns.values)[1]]
energyFormList = list(energy.columns.values)[1:-1]
i = 0
colors = list('rgbcmyk')
plt.figure('Energy consumption per country')
plt.title('Energy consumption per country')

for energyForm in energyFormList:
	i += 1
	ax = plt.subplot(6, 1, i)
	ax.set_xlim([0,65])
	plt.ylabel(energyForm)
	plt.bar(arange(65), energy[energyForm], color=colors[i],width=0.7)
	plt.grid(True)                                                  # zeichnet ein Raster
	plt.xticks(range(65), "")
plt.xticks(range(65), energy.Country, rotation='vertical', horizontalalignment='left')
plt.show()