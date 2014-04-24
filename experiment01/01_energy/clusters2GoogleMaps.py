import pandas
import pymaps
from pymaps import *

NUM_CLUSTER = 4
FIELDS = ['Country', 'Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro', 'Total2009', 'Lat', 'Long', 'clusterIndex']
NUM_FIELDS = len(FIELDS)

energyInfo = pandas.read_csv('EnergyMixGeo.csv')
reducedEnergyInfo = energyInfo[FIELDS]

map = PyMap()
icon1 = Icon('iconGreen')
icon2 = Icon('iconRed')
icon3 = Icon('iconBlue')
icon4 = Icon('iconYellow')
icon1.image = "http://labs.google.com/ridefinder/images/mm_20_green.png" # for testing only!
icon1.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png" # do not hotlink from your web page!
icon2.image = "http://labs.google.com/ridefinder/images/mm_20_red.png" # for testing only!
icon2.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png" # do not hotlink from your web page!
icon3.image = "http://labs.google.com/ridefinder/images/mm_20_blue.png" # for testing only!
icon3.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png" # do not hotlink from your web page!
icon4.image = "http://labs.google.com/ridefinder/images/mm_20_yellow.png" # for testing only!
icon4.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"

map.addicon(icon1)
map.addicon(icon2)
map.addicon(icon3)
map.addicon(icon4)

#map.maps[0].zoom = 10

map.key = 'AIzaSyDgR1sE91D1Tbl6FCKs5bU61IZhtzCM3nA'

q=[52,11]

map.maps[0].setpoint(q)
print open('clusterMap.html', 'wb').write(map.showhtml())