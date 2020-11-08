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
x = 'defecte spoorbrug'
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

zero = data.loc[data['start_month'] == 00]
min0 = januari['duration_minutes'].sum()

one = data.loc[data['start_month'] == 01]
min1 = februari['duration_minutes'].sum()

two = data.loc[data['start_month'] == 02]
min2 = maart['duration_minutes'].sum()

three = data.loc[data['start_month'] == 03]
min3 = april['duration_minutes'].sum()

four = data.loc[data['start_month'] == 04]
min4 = mei['duration_minutes'].sum()

five = data.loc[data['start_month'] == 05]
min5 = juni['duration_minutes'].sum()

six = data.loc[data['start_month'] == 06]
min6 = juli['duration_minutes'].sum()

seven = data.loc[data['start_month'] == 07]
min7 = augustus['duration_minutes'].sum()

eight = data.loc[data['start_month'] == 08]
min8 = september['duration_minutes'].sum()

nine = data.loc[data['start_month'] == 09]
min9 = oktober['duration_minutes'].sum()

ten = data.loc[data['start_month'] == 10]
min10 = november['duration_minutes'].sum()

eleven = data.loc[data['start_month'] == 11]
min11 = december['duration_minutes'].sum()

twelve = data.loc[data['start_month'] == 12]
min12 = december['duration_minutes'].sum()

thirteen = data.loc[data['start_month'] == 13]
min13 = december['duration_minutes'].sum()

fourteen = data.loc[data['start_month'] == 14]
min14 = december['duration_minutes'].sum()

fiveteen = data.loc[data['start_month'] == 15]
min15 = december['duration_minutes'].sum()

sixteen = data.loc[data['start_month'] == 16]
min16 = december['duration_minutes'].sum()

seventeen = data.loc[data['start_month'] == 17]
min17 = december['duration_minutes'].sum()

eighteen = data.loc[data['start_month'] == 18]
min18 = december['duration_minutes'].sum()

nineteen = data.loc[data['start_month'] == 19]
min19 = december['duration_minutes'].sum()

twenty = data.loc[data['start_month'] == 20]
min20 = december['duration_minutes'].sum()

twentyOne = data.loc[data['start_month'] == 21]
min21 = december['duration_minutes'].sum()

twentyTwo = data.loc[data['start_month'] == 22]
min22 = december['duration_minutes'].sum()

twentyThree = data.loc[data['start_month'] == 23]
min23 = december['duration_minutes'].sum()

lenmonths = [len(januari),len(februari), len(maart), len(april), len(mei), len(juni), len(juli), len(augustus), len(september), len(oktober),len(november), len(december)]
months = ["jan", "feb","mrt","apr","mei","jun","jul","aug","sep","okt","nov","dec"]
minutes = [minjan,minfeb,minmrt,minapr,minmei,minjun,minjul,minaug,minsept,minokt,minnov,mindec]
hours = ["00","01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16","17", "18", "19", "20", "21", "22", "23"]
lentimes = [len(zero), len(one), len(two), len(three), len(four), len(five), len(six), len(seven), len(eight), len(nine), len(ten), len(eleven), len(twelve), len(thirteen),
len(fourteen), len(fiveteen),len(sixteen),len(seventeen),len(eighteen), len(nineteen), len(twenty), len(twentyOne), len(twentyTwo), len(twentyThree)]
minutesperHour = [min0, min1, min2, min3, min4, min5, min6, min7, min8, min9, min10, min11, min12, min13, min14, min15, min16, min17, min18, min19, min20, min21, min22, min23]
print("Aantal minuten storing vanwege " + x + " per maand")
print(minutes)
print("Aantal " + x + " per maand")
print(lenmonths)
plt.bar(range(len(months)), lenmonths)
plt.xticks(range(len(months)), months)
plt.ylabel("Aantal")
plt.title("Aantal per maand: " + x)
#plt.show()

plt.bar(range(len(months)), minutes)
plt.xticks(range(len(months)), months)
plt.ylabel("Minutes")
plt.title("Minuten per maand: " + x)
#plt.show()

plt.bar(range(len(lentimes)), minutesperHour)
plt.xticks(range(len(hours)), hours)
plt.ylabel("Minutes")
plt.title("Minuten per uur: " + x)
#plt.show()

plt.bar(range(len(lentimes)), lentimes)
plt.xticks(range(len(hours)), hours)
plt.ylabel("Aantal")
plt.title("Aantal per uur: " + x)
#plt.show()
