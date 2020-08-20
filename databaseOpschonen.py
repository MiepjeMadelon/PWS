import numpy as np;
import pandas as pd;


#make the database ready
trainsData = pd.read_csv("disruptions-2011-2019.csv", names = ['rdt_id', 'ns_lines', 'rdt_lines', 'rdt_lines_id', 'rdt_station_names',
       'rdt_station_codes', 'cause_nl', 'cause_en', 'statistical_cause_nl',
       'statistical_cause_en', 'cause_group', 'start_time', 'end_time',
       'duration_minutes'], header = 0);


#cleaning up rows with missing time values

    #loop through rows
for row in trainsData:
    if 'start_time' == ' ' :
        data.drop(row, axis = 0 )


    #check if x is empty

    #if empty, remove entire row



#getting the math right (Yasmin)
