import pandas
from sklearn import feature_selection
from numpy import *
import matplotlib.pyplot as plt

NUM_CLUSTER = 4
ENERGYFORMS = ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']
TARGET = ['CO2Emm']
NUM_ENEGRYFORMS = len(ENERGYFORMS)

energyInfo = pandas.read_csv('../resources/EnergyMixGeo.csv')
reducedEnergyInfo = energyInfo[ENERGYFORMS]
targetInfo = energyInfo[TARGET]

featureSelector =  feature_selection.SelectKBest(score_func = feature_selection.f_regression, k = NUM_ENEGRYFORMS)

featureSelector.fit_transform(X = reducedEnergyInfo, y=targetInfo )

scoresArray = pandas.Series(featureSelector.scores_, reducedEnergyInfo.columns.values)
print scoresArray