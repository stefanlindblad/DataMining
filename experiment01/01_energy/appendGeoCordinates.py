
import pandas
from numpy import *
import matplotlib.pyplot as plt


energy = pandas.read_csv('../resources/EnergyMix.csv')


print
print energy.Oil
plt.bar(range(65), energy.Oil, color='r')
plt.bar(range(65), energy.Gas, color='b')
plt.bar(range(65), energy.Coal, color='g')
plt.xticks(range(65), energy.Country, rotation='vertical')
#plt.axis([0, 65, 0, 850])
plt.title('Oil in Country')
plt.ylabel('Oil in CO2 Eq')
plt.xlabel('Country')
plt.grid(True)                          # zeichnet ein Raster

plt.show()