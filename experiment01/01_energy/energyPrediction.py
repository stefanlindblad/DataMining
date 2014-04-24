import pandas
from sklearn import svm, cross_validation, feature_selection
from numpy import *
import matplotlib.pyplot as plt

NUM_CLUSTER = 4
ENERGYFORMS = ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']
TARGET = ['CO2Emm']
NUM_ENEGRYFORMS = len(ENERGYFORMS)

def crossValidateRegression(X, y, C, epsilon):
    svr = svm.SVR(kernel='linear', C=C, epsilon=epsilon)
    crossValidator = cross_validation.KFold(NUM_COUNTRYS, n_folds = 10)
    cross_validation.cross_val_score(svr, X, y, cv=crossValidator, scoring='mean_squared_error')
    svr.fit(X, y)
    predictedTargetInfo = svr.predict(X)
    return predictedTargetInfo

def mae(actual, predicted):
    return sum(abs(actual - predicted))/len(actual)

def plot(actual, predicted, C, epsilon, mae, colors=['g', 'r']):
    plt.figure()
    plt.plot(actual, color=colors[0], label='actual')
    plt.plot(predicted, color=colors[1], label='predicted')
    plt.legend()
    plt.annotate("C = "+str(C), xy=(2.5,7500))
    plt.annotate(u'\u03B5'+" = "+unicode(epsilon), xy=(2.5,7100))
    plt.annotate("MAE = " + str(mae), xy=(2.5,6700))
    plt.show()

def getInfo(actual, predicted, indices):
    frame = pandas.DataFrame(data=actual, index=indices, columns=['actual'])
    frame['predicted'] = pandas.Series(data=predicted, index=indices)
    frame['difference'] = actual - predicted
    return frame

energyInfo = pandas.read_csv('../resources/EnergyMixGeo.csv')
reducedEnergyInfo = energyInfo[ENERGYFORMS]
targetInfo = energyInfo[TARGET].values[:,0]
NUM_COUNTRYS = len(reducedEnergyInfo.values)


C=0.001
epsilon=0.1
predictedTargetInfo = crossValidateRegression(reducedEnergyInfo, targetInfo, C, epsilon)


mae = mae(targetInfo, predictedTargetInfo)
print "\nMean Absolute Error: " + str(mae)

plot(targetInfo, predictedTargetInfo, C, epsilon, mae)

print getInfo(targetInfo, predictedTargetInfo, energyInfo.Country.values)