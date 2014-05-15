# -*- coding:utf8 -*-
# author: Stefan Seibert
# File for task 3.1.2

import pandas as pd
from matplotlib import pyplot as plt
from sklearn import svm

def getMae(actual, predicted):
    return sum(abs(actual - predicted))/len(actual)

def getModel(delay, dataFrame ):
    columnNames = ["T-" + str(r) for r in range(delay,0,-1)]
    frame = pd.DataFrame( columns = columnNames).T
    series = pd.Series()
    for startvalue in range(0, len(dataFrame.index)-delay-1):
        array = dataFrame[startvalue : startvalue + delay].values
        frame[startvalue] = array
        series.set_value(startvalue, dataFrame[startvalue + delay])
    frame = frame.T
    return frame, series;



# reading in the csv file into a pandas dataframe
dataFrame = pd.DataFrame().from_csv("effectiveRates.csv")

# plotting the courses from sony, canon, cisco, hewlett-packard and yahoo
#plt.plot(dataFrame.index, dataFrame["SNE"], "bo-", color="c", ms=2, label="Sony")
#plt.plot(dataFrame.index, dataFrame["CAJ"], "bo-", color="m", ms=2, label="Canon")
#plt.plot(dataFrame.index, dataFrame["CSCO"], "bo-", color="r", ms=2, label="Cisco")
#plt.plot(dataFrame.index, dataFrame["HPQ"], "bo-", color="g", ms=2, label="Hewlett-Packard")
#plt.plot(dataFrame.index, dataFrame["YHOO"], "bo-", color="b", ms=2, label="Yahoo")

plt.legend(bbox_to_anchor=(1.05, 1), loc=2)


plt.ylabel("prices")
plt.xlabel("time")
plt.grid()
#plt.show()

TRAININGS_TIME = 650
PREDICTION_TIME = 30
TIME_DELAY = 24

model, target = getModel(TIME_DELAY, dataFrame["YHOO"])
trainData = model[:TRAININGS_TIME]
trainDataTargets = target[:TRAININGS_TIME]
dataToPredict = model[TRAININGS_TIME:TRAININGS_TIME+PREDICTION_TIME]

svr = svm.SVR(kernel="rbf", C=500, epsilon=.6)
svr.fit(trainData, trainDataTargets)

array = []
predictedValues = svr.predict(trainData)

for i in range(1, PREDICTION_TIME):
    predictedTarget = svr.predict(dataToPredict[i:i+1])
    array.append(predictedTarget[0])
    #print predictedTarget
    #print dataToPredict[i:i+1]

    for y in range(1, TIME_DELAY+1):
        dataToPredict.loc[i+y+649, "T-"+str(y)] = predictedTarget[0]


print len(array)

plt.figure("Yahoo Stock Prediction")

plt.plot(dataFrame.index, dataFrame["YHOO"], "b", color="b", ms=2, label="real")
plt.plot(dataFrame.index[23:673], predictedValues, "bo-", color="g", ms=2, label="predict")
plt.plot(dataFrame.index[673:702], array, "bo-", color="r", ms=2, label="forecast")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)

plt.ylabel("prices")
plt.xlabel("time")
#plt.grid()
plt.show()






