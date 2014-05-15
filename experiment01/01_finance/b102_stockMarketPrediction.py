# -*- coding:utf8 -*-
# author: Stefan Seibert
# File for task 3.1.2

import pandas as pd
from matplotlib import pyplot as plt

# reading in the csv file into a pandas dataframe
dataFrame = pd.DataFrame().from_csv("effectiveRates.csv")

# plotting the courses from sony, canon, cisco, hewlett-packard and yahoo
plt.plot(dataFrame.index, dataFrame["SNE"], "bo-", ms=2)
plt.plot(dataFrame.index, dataFrame["CAJ"], "bo-", ms=2)
plt.plot(dataFrame.index, dataFrame["CSCO"], "bo-", ms=2)
plt.plot(dataFrame.index, dataFrame["HPQ"], "bo-", ms=2)
plt.plot(dataFrame.index, dataFrame["YHOO"], "bo-", ms=2)
plt.ylabel("prices")
plt.xlabel("time")
plt.grid()
plt.show()

