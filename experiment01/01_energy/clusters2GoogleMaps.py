import pandas
import pymaps
from pymaps import *

FIELDS = ['Country', 'Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro', 'Total2009', 'Lat', 'Long', 'clusterIndex']

energyInfo = pandas.read_csv('EnergyMixGeo.csv')
reducedEnergyInfo = energyInfo[FIELDS]

map = PyMap()

icon1 = Icon('icon1')
icon2 = Icon('icon2')
icon3 = Icon('icon3')
icon4 = Icon('icon4')
icon1.image = "http://labs.google.com/ridefinder/images/mm_20_blue.png"
icon1.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"
icon2.image = "http://labs.google.com/ridefinder/images/mm_20_green.png"
icon2.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"
icon3.image = "http://labs.google.com/ridefinder/images/mm_20_red.png"
icon3.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"
icon4.image = "http://labs.google.com/ridefinder/images/mm_20_yellow.png"
icon4.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"
map.addicon(icon1)
map.addicon(icon2)
map.addicon(icon3)
map.addicon(icon4)

map.maps[0].zoom = 2

for index, country in enumerate(energyInfo.Country.values):
    countryInfo = country + ": "
    countryInfo += "Oil: " + str(energyInfo.Oil[index])
    countryInfo += ", Gas: " + str(energyInfo.Gas[index])
    countryInfo += ", Coal: " + str(energyInfo.Coal[index])
    countryInfo += ", Nuclear: " + str(energyInfo.Nuclear[index])
    countryInfo += ", Hydro: " + str(energyInfo.Hydro[index])
    countryInfo += ", Total: " + str(energyInfo.Total2009[index])
    map.maps[0].setpoint([energyInfo.Lat[index], energyInfo.Long[index], countryInfo, 'icon' + str(energyInfo.clusterIndex[index] + 1)])

##    print g.showhtml()
open('clustermap.html','wb').write(map.showhtml())   # generate test file