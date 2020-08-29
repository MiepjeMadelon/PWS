import numpy as np;
import pandas as pd;
from SDfunction import *

#make the database ready
#the names were already established, but now we can easily find them
trainsData = pd.read_csv("disruptions-2011-2019.csv", names = ['rdt_id', 'ns_lines', 'rdt_lines', 'rdt_lines_id', 'rdt_station_names',
       'rdt_station_codes', 'cause_nl', 'cause_en', 'statistical_cause_nl',
       'statistical_cause_en', 'cause_group', 'start_time', 'end_time',
       'duration_minutes'], header = 0);
trainsData = pd.DataFrame(trainsData)

#cleaning up rows with missing time values by looping through each row,
#check for empty values, and if one is empty drop the row.
#I dont know how to select the empty value. ' ' (V1), ''(V2) and None(V3) don't work
#I removed the axis = 0 from data.drop(). It still doesn't work (V4)
    #loop through rows
#for index, row in trainsData:
    #if 'start_time' == 'nan' or 'duration_minutes' == 'nan' or 'cause_nl' == 'nan' or 'cause_en' == 'nan' or 'statistical_cause_en' == 'nan' or 'statistical_cause_nl' == 'nan': #see line 44 for nan
        #trainsData.drop(row, axis = 0)
        #trainsData.to_csv(r'../CleanDataV8.csv')

#I saw this code to drop rows on stackoverflow (V5)
#It removes a lot of data, but now even more cells are empty.
#I commented this code out
#trainsData = trainsData.dropna(how='any',axis=0)
#trainsData.to_csv(r'../CleanDataV5.csv')

#trying to test if the code on line 18 works by dropping all rows (V6)
#this doesn't do anything. I think the loop doesn't work correctly
#for row in trainsData:
    #trainsData.drop(row, axis = 1)
    #trainsData.to_csv(r'../CleanDataV6.csv')
#to test this I'll print each row
#for row in trainsData:
#    print();
#it only prints the first row.
#for index, row in trainsData:
    #print();
#now it works, however, there are too many values to unpack
#I'll change each for loop into the working varient (V7 with None).
#ValueError: too many values to unpack (expected 2)
#Trying to figure out which value pandas assingns for empty cells by selecting one (looked it up via excel)
# print(trainsData.loc[170,'cause_nl']) returns nan


#now I'm setting up a while loop to later make it iterate through rows using the index
#condition = len(trainsData)-1; #there now seems to be an extra row, I think it calculates the header as a row
#tel = 0
#print(trainsData.count())
#while condition >= 0: #1 because the len is including the header
    #if condition == 0:
        #print(trainsData.loc[[condition]]) #print rij met index 0, dus nu staat condition gelijk aan row nummers
#trainsData.dropna() #before trainsData.replace = V8

# replace field that's entirely space (or empty) with NaN
#trainsData.replace(r'\s+', np.nan, regex=True)
trainsData.dropna( #this now gives very weird results (V9_7)
    axis=0,
    how='any',
    thresh=None,
    inplace=True,
    subset=['cause_nl', 'cause_en', 'statistical_cause_nl', 'statistical_cause_en', 'cause_group', 'start_time', 'end_time', 'duration_minutes']
)
contains_NaN = trainsData.isna().any(axis=None)
#print(contains_NaN)

#trainsData.to_csv(r'CleanDataNV1.csv')
#IT WORKS!!!!!!!!!!

#Now we have to remove the outliers using the code from the SD.py and SDfunction.py files
minutes = trainsData['duration_minutes'].tolist() #takes the column duration_minutes and puts it in a list
SD = int(calculateSD(trainsData, 'duration_minutes'))  #calculates the SD of the column
mean = int(calculateMean(trainsData, 'duration_minutes')) #calculated the mean of the column
SDhigh = mean+3*SD #calculates the high outlier using the empirical rule
SDlow = mean-3*SD #calculates the low outlier using the empirical rule
print(SD)#prints the SD to compare the beginning value with the end value


#The more I look at it, the less I think the SD should be recalculated, so I hashed this code out
#loops through each number to check if it is higher than the SD*3
#If it is higher, than it removes it.
#After all these values are removed, it recalculates the SD*3 until nothing is higher than that.
#while np.any(i > SD3 for i in minutes): #used to be >=, it doesnt matter for the outcome
    #trainsData = trainsData[trainsData['duration_minutes'] <= SD3] #used to be >=, this caused an infinite loop so I changed it to <=. Then to <
    #minutes = trainsData['duration_minutes'].tolist()
    #SD3 = int(calculateSD(trainsData, 'duration_minutes'))
    #print(SD3) #it seems that this while statement is an infinite loop, with this I want to test that
    #this loop is an infinite loop, since eventually it just keeps printing 1277
    #changed >= to <= in line 79, now it prints the following 611,105,30,8,2,0 and keeps printing 0.
    #changed <= to <, but now it keeps removing all values.
#while np.any(i >= SDhigh for i in minutes): #used to be >=, it doesnt matter for the outcome
    #trainsData = trainsData[trainsData['duration_minutes'] < SDhigh] #used to be >=, this caused an infinite loop so I changed it to <=. Then to <
    #minutes = trainsData['duration_minutes'].tolist()
    #SD = int(calculateSD(trainsData, 'duration_minutes')) #calculates the SD of the column
    #mean = int(calculateMean(trainsData, 'duration_minutes'))
    #SDhigh = mean+3*SD
    #print(SDhigh) #to see how the values changed and to confirm it is an infinite loop
    #print(SD3)


#New progress: The empirical rule (what we did above) should only be calculated ONCE
#so this will give us the following:
#remove all high outliers:
trainsData = trainsData[trainsData['duration_minutes'] < SDhigh]
trainsData = trainsData[trainsData['duration_minutes'] > SDlow]
trainsData.to_csv(r'CleanDataNV2.csv')
