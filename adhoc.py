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
x = 'inzet van hulpdiensten'
data = data.loc[data['cause_nl'] == x]
#lets firt make a table with the months and how many minutes it'll take.
januari = data.loc[data['start_month'] == 1]
minjan = januari['duration_minutes'].sum()

februari = data.loc[data['start_month'] == 2]
minfeb = februari['duration_minutes'].sum()

maart = data.loc[data['start_month'] == 3]
minmrt = maart['duration_minutes'].sum()

april = data.loc[data['start_month'] == 4]
minapr = april['duration_minutes'].sum()

mei = data.loc[data['start_month'] == 5]
minmei = mei['duration_minutes'].sum()

juni = data.loc[data['start_month'] == 6]
minjun = juni['duration_minutes'].sum()

juli = data.loc[data['start_month'] == 7]
minjul = juli['duration_minutes'].sum()

augustus = data.loc[data['start_month'] == 8]
minaug = augustus['duration_minutes'].sum()

september = data.loc[data['start_month'] == 9]
minsept = september['duration_minutes'].sum()

oktober = data.loc[data['start_month'] == 10]
minokt = oktober['duration_minutes'].sum()

november = data.loc[data['start_month'] == 11]
minnov = november['duration_minutes'].sum()

december = data.loc[data['start_month'] == 12]
mindec = december['duration_minutes'].sum()

lenmonths = [len(januari),len(februari), len(maart), len(april), len(mei), len(juni), len(juli), len(augustus), len(september), len(oktober),len(november), len(december)]
months = ["jan", "feb","mrt","apr","mei","jun","jul","aug","sep","okt","nov","dec"]
minutes = [minjan,minfeb,minmrt,minapr,minmei,minjun,minjul,minaug,minsept,minokt,minnov,mindec]
print("Aantal minuten storing vanwege " + x + " per maand")
print(minutes)
print("Aantal " + x + " per maand")
print(lenmonths)
plt.bar(range(len(months)), lenmonths)
plt.xticks(range(len(months)), months)
plt.ylabel("Aantal")
plt.title("Aantal per maand: " + x)
plt.show()

plt.bar(range(len(months)), minutes)
plt.xticks(range(len(months)), months)
plt.ylabel("Minutes")
plt.title("Minuten per maand: " + x)
#plt.show()
