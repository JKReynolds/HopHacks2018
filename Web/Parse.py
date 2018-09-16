import csv
def read_data(dataFile):
         # Reads csv file
    dataSet = []
    dataSetDecode = []
    dataSetTime = []
    timeHolder = []
    with open(dataFile, "rb") as csvfile:
        for row in csvfile:
            dataSet.append(row) #for loop which converts all rows into 4-element lists
    for row in dataSet:
        dataSetDecode.append(row.decode("utf-8"))
    for row in range(len(dataSetDecode)):
        timeHolder.append(0)
        dataSetDecode[row] = dataSetDecode[row].rstrip()
            
        dataSetDecode[row] = dataSetDecode[row].split(",")
        dataSetDecode[row].append(dataSetDecode[row][2])
        dataSetDecode[row][3] = dataSetDecode[row][3][:21]
    for row in range(len(dataSetDecode)):
        for col in range(2):
            dataSetDecode[row][col] = float(dataSetDecode[row][col])
        for col in range(2, 4):
            dataSetDecode[row][col] = dataSetDecode[row][col].lstrip()
            dataSetDecode[row][col] = dataSetDecode[row][col].lstrip("\'")
                
        dataSetDecode[row][2] = dataSetDecode[row][2][8:10]
        if (dataSetDecode[row][2][0] == "0"):
            dataSetDecode[row][2] = dataSetDecode[row][2][1]
        else:
            dataSetDecode[row][2] = dataSetDecode[row][2][0:2]
        
        dataSetDecode[row][2] = int(dataSetDecode[row][2])
        dataSetDecode[row][3] = dataSetDecode[row][3][11:]
        
        dataSetTime.append(dataSetDecode[row][3])
        dataSetDecode[row] = dataSetDecode[row][:3]
        timeHolder[row] = (3600 * int(dataSetTime[row][:2]) + 60 * int(dataSetTime[row][3:5]) + int(dataSetTime[row][6:]))
        dataSetDecode[row].append(timeHolder[row])
        
        #for row in range(len(timeHolder)):
            
        
        #time = (3600 * int(clock[:2]) + 60 * int(clock[3:5]) + int(clock[6:]))"""
        
    return dataSetDecode
"""    
print(read_data("freshTrainingData2.csv")[0])
print(read_data("freshTrainingData2.csv")[1])
print(read_data("freshTrainingData2.csv")[2])
print(read_data("freshTrainingData2.csv")[3])

print(read_data("badTrainingData2.csv")[0])
print(read_data("badTrainingData2.csv")[1])
print(read_data("badTrainingData2.csv")[2])
print(read_data("badTrainingData2.csv")[3])
"""