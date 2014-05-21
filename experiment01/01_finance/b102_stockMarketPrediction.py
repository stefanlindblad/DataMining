# -*- coding:utf8 -*-
# author: Stefan Seibert
# File for task 3.1.2

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import svm

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def getmae(actual, predicted):
    return sum(abs(actual - predicted))/len(actual)

def getmodel(daysUsedForEstimation, dataframe):
    columnnames = ["T-" + str(r) for r in range(daysUsedForEstimation, 0, -1)] #excluding the zero
    model = pd.DataFrame(columns=columnnames).T # having a list of days with values before the actual day, for everyday
    target = pd.Series() #a list of the values that the value really has normally

    for currentCalculatedDay in range(0, len(dataframe.index)-daysUsedForEstimation):
        model[currentCalculatedDay] = dataframe[currentCalculatedDay: currentCalculatedDay + daysUsedForEstimation].values
        target.set_value(currentCalculatedDay, dataframe[currentCalculatedDay + daysUsedForEstimation])

    model = model.T
    return model, target;

# reading in the csv file into a pandas dataframe
dataFrame = pd.DataFrame().from_csv("effectiveRates.csv")

# plotting the courses from sony, canon, cisco, hewlett-packard and yahoo
plt.figure("compartment of different companies")
plt.plot(dataFrame.index, dataFrame["SNE"], "bo-", color="c", ms=2, label="Sony")
plt.plot(dataFrame.index, dataFrame["CAJ"], "bo-", color="m", ms=2, label="Canon")
plt.plot(dataFrame.index, dataFrame["CSCO"], "bo-", color="r", ms=2, label="Cisco")
plt.plot(dataFrame.index, dataFrame["HPQ"], "bo-", color="g", ms=2, label="Hewlett-Packard")
plt.plot(dataFrame.index, dataFrame["YHOO"], "bo-", color="b", ms=2, label="Yahoo")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.ylabel("prices")
plt.xlabel("time")
plt.grid()

# Script Variables, change them for different behaviour
TRAININGS_TIME = 650
PREDICTION_TIME = 30
TIME_DELAY = 24
C_VALUE = 0.0005
EPSILON_VALUE = 0.06

# getting model and target
model, target = getmodel(TIME_DELAY, dataFrame["YHOO"])

# defining the learning period
trainData = model[:TRAININGS_TIME+1]
trainDataTargets = target[:TRAININGS_TIME+1]
predictionData = model[TRAININGS_TIME+1:TRAININGS_TIME+PREDICTION_TIME+1]

# fitting the SVR to our data
svr = svm.SVR(kernel="rbf", C=C_VALUE, epsilon=EPSILON_VALUE)
svr.fit(trainData, trainDataTargets)

forecastValues = []
predictedValues = svr.predict(trainData)

for i in range(0, PREDICTION_TIME):
    forecastValue = svr.predict(predictionData[i:i+1])
    forecastValue = forecastValue[0]
    forecastValues.append(forecastValue)

    for y in range(1, TIME_DELAY+1):
        predictionData.loc[i+y+TRAININGS_TIME, "T-"+str(y)] = forecastValue

forecastValues = pd.Series(forecastValues, index = dataFrame["YHOO"][TRAININGS_TIME+TIME_DELAY+1:TRAININGS_TIME+TIME_DELAY+PREDICTION_TIME+1].index)

mae = getmae(dataFrame["YHOO"][TRAININGS_TIME+TIME_DELAY+1:TRAININGS_TIME+TIME_DELAY+PREDICTION_TIME+1], forecastValues)
print "Mean Absolute Error: " + str(mae) + ", C = " + str(C_VALUE) + ", epsilon = " + str(EPSILON_VALUE) + ", delay = " + str(TIME_DELAY)

plt.figure("Yahoo Stock Prediction")
plt.plot(dataFrame.index, dataFrame["YHOO"], "b", color="b", ms=2, label="real")
plt.plot(dataFrame.index[TIME_DELAY:TRAININGS_TIME+TIME_DELAY+1], predictedValues, "bo-", color="g", ms=2, label="predict")
plt.plot(dataFrame.index[TRAININGS_TIME+TIME_DELAY+1:TRAININGS_TIME+TIME_DELAY+PREDICTION_TIME+1], forecastValues, "bo-", color="r", ms=2, label="forecast")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.ylabel("prices")
plt.xlabel("time")
plt.grid()
plt.show()