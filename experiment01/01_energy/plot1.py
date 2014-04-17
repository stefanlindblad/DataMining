
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

for energyForm in energyFormList:
	print colors[i]
	plt.bar(arange(65) + (width * i), energy[energyForm], width, color=colors[i], label=energyForm)
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
	i += 1

plt.xticks(range(65), energy.Country, rotation='vertical')
plt.title('Energy consupmtion per country')
plt.ylabel('Consumption in CO2 eq')
plt.grid(True)                          # zeichnet ein Raster
plt.autoscale()
plt.show()