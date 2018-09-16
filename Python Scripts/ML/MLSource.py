import numpy as np
from sklearn import datasets
from sklearn import svm
import sklearn.datasets
import csv
import Parse


#nX = import open("", "rb")
normalData = Parse.read_data("freshTrainingData2.csv")[:5000]
alertData1 = Parse.read_data("badTrainingData1.csv")[:5000]
alertData2 = Parse.read_data("badTrainingData2.csv")[:5000]
nX = np.array(alertData1[:5000] + normalData[:5000] + alertData2[:5000])     #Initalize and set Samples/Features [double lat, double long, int day, double time] 
nYb1 = np.ones(len(alertData1))[:5000]          
nYn = np.zeros(len(normalData))[:5000] 
nYb2 = np.ones(len(alertData2))[:5000]
nY = np.concatenate((nYb1, nYn, nYb2), axis=0)                  #Initialize and set Targets 0=normal, 1=alert
greekTown = sklearn.datasets.base.Bunch(data=nX, target=nY)                  #Initialize and set database (tuple[][] data, tuple[] target)

clf = svm.SVC()                                              #Initialize estimator from sklearn svm

clf.fit(greekTown.data[:-1], greekTown.target[:-1])                #method fit gives estimator clf supervised data with targets, except for last element
print(clf.predict(greekTown.data[-1:]))
print(clf.predict(np.array([[39.2839849, -76.5475151, 1, 3000]])))  #prediction on I-95                        #prints estimator predition for last element
print(clf.predict(np.array([[39.1808143, -78.7451911, 1, 3000]])))
print(clf.predict(np.array([[39.2871325, -76.5534954, 1, 3000]])))


############################################
## Second set of data
############################################

normalData = Parse.read_data("freshTrainingData2.csv")[5000:10000]
alertData1 = Parse.read_data("badTrainingData1.csv")[5000:10000]
alertData2 = Parse.read_data("badTrainingData2.csv")[5000:10000]
nX = np.array(alertData1[5000:10000] + normalData[5000:10000] + alertData2[5000:10000])     #Initalize and set Samples/Features [double lat, double long, int day, double time] 
nYb1 = np.ones(len(alertData1))[5000:10000]          
nYn = np.zeros(len(normalData))[5000:10000] 
nYb2 = np.ones(len(alertData2))[5000:10000]
nY = np.concatenate((nYb1, nYn, nYb2), axis=0)                  #Initialize and set Targets 0=normal, 1=alert
greekTown = sklearn.datasets.base.Bunch(data=nX, target=nY)                  #Initialize and set database (tuple[][] data, tuple[] target)

clf = svm.SVC()                                              #Initialize estimator from sklearn svm

clf.fit(greekTown.data[:-1], greekTown.target[:-1])                #method fit gives estimator clf supervised data with targets, except for last element
print(clf.predict(greekTown.data[-1:]))
print(type(greekTown.data[-1:]))
print(clf.predict(np.array([[39.2839849, -76.5475151, 1, 3000]])))  #prediction on I-95                        #prints estimator predition for last element
print(clf.predict(np.array([[39.1808143, -78.7451911, 1, 3000]])))  #West Virginia
print(clf.predict(np.array([[39.2871325, -76.5534954, 1, 3000]])))  #895

