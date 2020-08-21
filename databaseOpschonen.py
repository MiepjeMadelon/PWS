import numpy as np;
import pandas as pd;


#make the database ready
#the names are already established, but now we can easily find them
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
for row in trainsData:
    if 'start_time' == None or 'duration_minutes' == None or 'cause_nl' == None or 'cause_nl' == None or 'statistical_cause_en' == None or 'statistical_cause_nl' == None:
        data.drop(row)


#I saw this code to drop rows on stackoverflow (V5)
#It removes a lot of data, but now even more cells are empty.
trainsData = trainsData.dropna(how='any',axis=0)
#trainsData.to_csv(r'../CleanDataV5.csv')

#getting the math right (Yasmin)
