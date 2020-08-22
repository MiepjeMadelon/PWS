import numpy as np;
import pandas as pd;


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
condition = len(trainsData)-1;
tel = 0
while condition > 1: #1 because the len is including the header
    condition -= 1
    tel += 1
print(condition)
print(tel)
