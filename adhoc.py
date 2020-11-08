from counter import *
import collections
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import csv

        #'rdt_id', 'ns_lines', 'rdt_lines', 'rdt_lines_id', 'rdt_station_names',
       #'rdt_station_codes', 'cause_nl', 'cause_en', 'statistical_cause_nl',
       #'statistical_cause_en', 'cause_group', 'start_time', 'end_time',
       #'duration_minutes', 'start_date', 'start_moment', 'start_year',
       #'start_month', 'start_day', 'start_hour', 'start_minute', 'start_second'

trainsData = pd.read_csv("output_6.csv", names = ['rdt_id', 'ns_lines', 'rdt_lines', 'rdt_lines_id', 'rdt_station_names',
       'rdt_station_codes', 'cause_nl', 'cause_en', 'statistical_cause_nl',
       'statistical_cause_en', 'cause_group', 'start_time', 'end_time',
       'duration_minutes', 'start_date', 'start_moment', 'start_year',
       'start_month', 'start_day', 'start_hour', 'start_minute', 'start_second'], header = 0);
data = pd.read_csv('output_6.csv')
