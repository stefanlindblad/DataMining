
import pandas
from numpy import *
import matplotlib.pyplot as plt


energy = pandas.read_csv('../resources/EnergyMix.csv')


print energy[list(energy.columns.values)[1]]
energyFormList = list(energy.columns.values)[1:-2]
i = 0
width = 0.15
colors = list('rgbcmyk')
plt.figure(1)
plt.title('Energy consupmtion per country')

for energyForm in energyFormList:
	print colors[i]
	i += 1
	plt.subplot(5, 1, i)
	plt.ylabel(energyForm)
	plt.bar(arange(65), energy[energyForm], color='c')
	plt.grid(True)                          # zeichnet ein Raster


plt.xticks(range(65), energy.Country, rotation='vertical')
plt.autoscale()
plt.show()