
import pandas
import matplotlib.pyplot as plt



ENERGYFORMS = ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']
NUM_ENERGYFORMS = len(ENERGYFORMS)

energyInfo = pandas.read_csv('../resources/EnergyMixGeo.csv')
print energyInfo.describe()

energyFormList = list(energyInfo.columns.values)[1:-2]
reducedEnergyInfo = energyInfo[ENERGYFORMS]

plt.figure("Energyconsumption by energyform in seperate subboxplots")
i = 0
for energyForm in reducedEnergyInfo:
	i += 1
	plt.subplot(1, 5, i)
	plt.xlabel(energyForm)
	plt.boxplot(energyInfo[energyForm].values, sym='')
	plt.grid(True)

plt.figure("Energyconsumption by energyform in one plot")
plt.boxplot(reducedEnergyInfo.values, sym='')
plt.xticks(range(1, NUM_ENERGYFORMS+1), ENERGYFORMS)
plt.show()