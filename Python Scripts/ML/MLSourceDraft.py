import numpy as np
from sklearn import datasets
from sklearn import svm
import sklearn.datasets

#from ParseGPStoML.py import open("", "rb")
#nX = import open("", "rb")
nX = np.array([[1.0,1.0,1, 1.0], [2.0,2.0,1, 2.0], [3.0,3.0,1, 3.0], [4.0,4.0,1, 4.0], [5.0,5.0,1, 5.0],
               [5.0,5.0,1, 1.0], [1.0,1.0,1, 5.0], [1.0,1.0,1, 4.0]])     #Initalize and set Samples/Features [double lat, double long, int day, double time] 
nY = np.array([1,1,1,1,1,0,0,0])                                          #Initialize and set Targets 0=normal, 1=alert
digits = sklearn.datasets.base.Bunch(data=nX, target=nY)                  #Initialize and set database (tuple[][] data, tuple[] target)

clf = svm.SVC()                                              #Initialize estimator from sklearn svm

clf.fit(digits.data[:-1], digits.target[:-1])                #method fit gives estimator clf supervised data with targets, except for last element
print(clf.predict(digits.data[-1:]))                         #prints estimator predition for last element

