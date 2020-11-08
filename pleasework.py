import pandas as pd
import collections
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import csv

trainsData = pd.read_csv("CleanDataNV5.csv", names = ['rdt_id', 'ns_lines', 'rdt_lines', 'rdt_lines_id', 'rdt_station_names',
       'rdt_station_codes', 'cause_nl', 'cause_en', 'statistical_cause_nl',
       'statistical_cause_en', 'cause_group', 'start_time', 'end_time',
       'duration_minutes'], header = 0);
data = pd.read_csv('CleanDataNV5.csv')

#for row in data:
#       if len(row) > 14:
#           datum = row[13].split('-') [0]
#
#print(datum)

#outfilename = "hopefully.csv"
#
#with open(trainsData, 'rb') as fp_in, open(outfilename, 'wb') as fp_out:
#    reader = csv.reader(fp_in, delimiter=",")
#    headers = next(reader)  # reads first row
#
#    writer = csv.writer(fp_out, delimiter=",")
#    writer.writerow(headers + ['datum'])
#
#    for row in reader:
#        if len(row) > 3:
#            # make sure there are at least 4 columns
#            datum = row[3].split('-', 1)[0]
#        writer.writerow(row + [datum])
#
#print(datum)

#def rename_email(row):
#    return row.start_time()
#
#data['datum'] = data.apply(rename_email, axis = 1)

#"""axis = 1 or 'columns': apply function to each row"""


#for row in data:
#       datum = data.start_time.split("-") [0]



print([start_time[i:i+2] for i in range(0, len(start_time), 3)])
