import pandas as pd
import collections
import numpy as np
import matplotlib.pyplot as plt
import statistics as st

#kopieer dit en hopelijk werkt het
trainsData = pd.read_csv("CleanDataNV5.csv", names = ['rdt_id', 'ns_lines', 'rdt_lines', 'rdt_lines_id', 'rdt_station_names',
       'rdt_station_codes', 'cause_nl', 'cause_en', 'statistical_cause_nl',
       'statistical_cause_en', 'cause_group', 'start_time', 'end_time',
       'duration_minutes'], header = 0);
data = pd.read_csv('CleanDataNV5.csv')

#probeer de x en de y-as rijtjes te geven uit de database




#oorzaken = ['cause_nl']

#gekopieerd van StackOverflow, hopelijk pakt dit de hele lijst ipv alleen cause_nl zelf
#oorzaken = data.cause_nl.tolist()
#Oke dat werkte ook niet

df = pd.DataFrame(data)
df = df[['cause_nl']]

oorzaken = df['cause_nl'].tolist()
#print (oorzaken)
#Ik ben dom...

#telt hoe vaak cause_nl erin voorkomt
#hoeVaak = Counter(['cause_nl'])

#hoeVaak = Counter(oorzaken)
#hoeVaak = Counter([oorzaken])

hoeVaak = collections.Counter(oorzaken)

#tel er 5 bij op zodat het de bar in het midden komt yay
#plt.bar([x + 5 for x in hoeVaak.keys()], hoeVaak.values(), 10, edgecolor=(0, 0, 0))

#het werkt eindelijk, je kan er niet 5 bij op tellen om het in het midden te zetten
plt.bar(range(len(oorzaken)), hoeVaak.values())

plt.title('Please Work')
plt.ylabel('aantal keren')

plt.xticks(range(len(oorzaken)), hoeVaak.values())

plt.show()
#eerst proberen met soorten en aantal oorzaken 4 okt 13:00
