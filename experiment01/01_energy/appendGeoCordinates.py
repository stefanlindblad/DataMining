import pandas
from numpy import *
from googlemaps import GoogleMaps

energy = pandas.read_csv('../resources/EnergyMix.csv')
gmaps = GoogleMaps(api_key = 'AIzaSyDgR1sE91D1Tbl6FCKs5bU61IZhtzCM3nA')

latList = []
lonList = []

for country in energy.Country:
    lat, lon = gmaps.address_to_latlng(country)
    latList.append(lat)
    lonList.append(lon)

energy['lat'] = pandas.Series(latList)
energy['lon'] = pandas.Series(lonList)

energy.to_csv('EnegryMixGeo.csv');