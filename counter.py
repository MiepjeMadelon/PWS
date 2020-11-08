import pandas as pd
import collections
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import csv

trainsData = pd.read_csv("output_6.csv", names = ['rdt_id', 'ns_lines', 'rdt_lines', 'rdt_lines_id', 'rdt_station_names',
       'rdt_station_codes', 'cause_nl', 'cause_en', 'statistical_cause_nl',
       'statistical_cause_en', 'cause_group', 'start_time', 'end_time',
       'duration_minutes', 'start_date', 'start_moment', 'start_year',
       'start_month', 'start_day', 'start_hour', 'start_minute', 'start_second'], header = 0);
data = pd.read_csv('output_6.csv')

#df_result = data['start_year'].count()
#print(df_result)

num_rdt_id = data['rdt_id'].value_counts()
#print(num_rdt_id)

num_ns_lines = data['ns_lines'].value_counts()
#print(num_ns_lines)

num_rdt_lines = data['rdt_lines'].value_counts()
#print(num_rdt_lines)

num_rdt_lines_id = data['rdt_lines_id'].value_counts()
#print(num_rdt_lines_id)

num_rdt_station_names = data['rdt_station_names'].value_counts()
#print(num_rdt_station_names)

num_rdt_station_codes = data['rdt_station_codes'].value_counts()
#print(num_rdt_station_codes)

num_cause_nl = data['cause_nl'].value_counts()
#print(num_cause_nl)

num_cause_en = data['cause_en'].value_counts()
#print(num_cause_en)

num_statistical_cause_nl = data['statistical_cause_nl'].value_counts()
#print(num_statistical_cause_nl)

num_statistical_cause_en = data['statistical_cause_en'].value_counts()
#print(num_statistical_cause_en)

num_cause_group = data['cause_group'].value_counts()
#print(num_cause_group)

num_start_time = data['start_time'].value_counts()
#print(num_start_time)

num_end_time = data['end_time'].value_counts()
#print(num_end_time)

num_duration_minutes = data['duration_minutes'].value_counts()
#print(num_duration_minutes)

num_start_date = data['start_date'].value_counts()
#print(num_start_date)

num_start_moment = data['start_moment'].value_counts()
#print(num_start_moment)

num_start_year = data['start_year'].value_counts()
#print(num_start_year)

num_start_month = data['start_month'].value_counts()
#print(num_start_month)

num_start_day = data['start_day'].value_counts()
#print(num_start_day)

num_start_hour = data['start_hour'].value_counts()
#print(num_start_hour)

num_start_minute = data['start_minute'].value_counts()
#print(num_start_minute)

num_start_second = data['start_second'].value_counts()
#print(num_start_second)






#jaren = Counter(data['start_year'])
#print(jaren)

#print(data['start_year'])  #test
