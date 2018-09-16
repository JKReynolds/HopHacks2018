from math import sin, cos, sqrt, atan2, radians
import pprint as pp
import datetime
import time
import csv

home = [39.286663, -76.557148]
lunch = [39.285974, -76.556053]

def incrDay(theDate):
    pre=theDate[:-2]
    post=int(theDate[-2:])
    post+=1
    return pre+"0"+str(post)

def pullInCSV():
    dataArr = []
    tmpArr = []
    tmpArr2 = []
    
    with open('data/trainWeekBad.csv','r') as trainingData:
        new_reader = csv.reader(trainingData)
        for line in new_reader:
            dataArr.append(line)
        for record in dataArr:
            for i in range(len(record)):
                if i<2:
                    record[i]=float(record[i])
                else:
                    record[i]=int(record[i])
        trainingData.close()
        # print(len(dataArr))
        # pp.pprint(dataArr)
        return dataArr
    

def timeIncrement(currentTime):
    #"2018-09-15 01:24:00 +0000"
    tempDate = str(currentTime)[:10]
    # print(tempDate)
    tempTime = str(currentTime)[10:20]
    # print(tempTime)
    tempSec = int(tempTime[-3:-1].replace(":",""))
    #print(tempSec)
    tempMin = int(tempTime[-6:-4].replace(":",""))
    # print(tempMin)
    tmpHr = int(tempTime[:-7].replace(" ",""))
    # print(tmpHr)

    tempSec+=1

    if (tempSec==60):
        #print("Minute increase")
        tempMin+=1
        tempSec = 0
        if (tempMin==60):
            #print("hour increase")
            tmpHr+=1
            tempMin=0
            if(tmpHr==24):
                tmpHr=0
                tempDate=incrDay(tempDate)
            
    
    if (tempSec<10):
        tempSec = "0"+str(tempSec)
    if (tempMin<10):
        tempMin = "0"+str(tempMin)
    if (tmpHr<10):
        tmpHr = "0"+str(tmpHr)


    returnString = ((str(tempDate + " " + str(tmpHr) + ":" + str(tempMin) + ":" + str(tempSec) + " +0000")))
    #print(returnString)
    return(returnString)

def genGPSdata(numStops,stopLocationArray,startTime,samplesPerHour):
    GPSdataArray = []
    locOne = [0,0,0] #lat,long, speed after this point
    locTwo = [0,0,0]
    latDif = 0
    longDif = 0
    latSampleIncr = 0
    longSampleIncr = 0
    sampleLat = 0
    sampleLong = 0
    distance = 0 #km
    time = 0 #in minutes
    numSample = 0
    currentTime = startTime
    timeSample = 0
    timeIncr = 1

    for stop in range(1,numStops):
        locOne = stopLocationArray[stop-1]
        locTwo = stopLocationArray[stop]
        distance = getDistance(locOne[0],locOne[1],locTwo[0],locTwo[1])
        time = locOne[2]
        numSample = round(time*samplesPerHour)

        latDif = locTwo[0]-locOne[0]
        longDif = locTwo[1]-locOne[1]
        latSampleIncr = latDif/numSample
        longSampleIncr = longDif/numSample
        sampleLat = locOne[0]
        sampleLong = locOne[1]
        
        for s in range(numSample):
            currentTime=timeIncrement(currentTime)
            sampleLat += latSampleIncr
            sampleLong += longSampleIncr
            timeSample += timeIncr
            GPSdataArray.append([sampleLat,sampleLong,currentTime])

    return GPSdataArray



def getDistance(latOne,longOne,latTwo,longTwo):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(latOne)
    lon1 = radians(longOne)
    lat2 = radians(latTwo)
    lon2 = radians(longTwo)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance




finalTrainingDataOut = genGPSdata(66,pullInCSV(),"2018-09-02 00:00:00 +0000",60)
# pp.pprint(finalTrainingDataOut)

fOut = open('data/badTrainingData2.csv','w')
for line in finalTrainingDataOut:
    fOut.write(str(line).replace("[","").replace("]","")+"\n")
fOut.close()

# home = [39.286663, -76.557148]
# lunch = [39.285974, -76.556053]

# pullInCSV()