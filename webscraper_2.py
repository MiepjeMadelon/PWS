import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from counter import *
import collections
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import csv
import re


#ik wil kijken of ik x kan opbouwen uit 3 variabelen, het jaar, de maand en dag
#jaar moet van 2018 t/m 2020
#maand moet van 1 t/m 12
#dag moet van 1 t/m 31
#j='2020'
year = [];
months = [];
days = [];
numTrains = [];

years=[2019, 2020]
for j in years:
    k=str(j)
    for m in range(12):
        n=str(m+1)
        for d in range(31):
            e=str(d+1)
            x = k + '-' + n + '-' + e
#            print(x)   #test

            if x=='2019-2-29' or x=='2019-2-30' or x=='2019-2-31' or x=='2019-4-31' or x=='2019-6-31' or x=='2019-9-31' or x=='2019-11-31' or x=='2020-2-30' or x=='2020-2-31' or x=='2020-4-31' or x=='2020-6-31' or x=='2020-9-31' or x=='2020-11-31':
                continue
            print(x)

            URL = 'https://www.rijdendetreinen.nl/treinarchief/{}/utrecht-centraal'.format(x)
#            print(URL) #test

#trein = requests.get(URL)

#soup = BeautifulSoup(trein.content, 'html.parser')

#results = soup.find(id = 'w0')

#python_jobs = results.find(class = 'container')

#for python_job in python_jobs:
#    print(python_job, end = '\n'*2)

#print(len(python_jobs))

#https://realpython.com/python-web-scraping-practical-introduction/#your-first-web-scraper

            page = urlopen(URL)
            year.append(int(k));
            months.append(int(n));
            days.append(int(e));

            html_bytes = page.read()
            html = html_bytes.decode("utf-8")

            start_index = html.find('<td>') + len('<td>')
            end_index = html.find('</td>',start_index)
            table = html[start_index:end_index]
            table.rstrip()
            table.strip()
            table = re.sub(r'[^\w\s]','',table)
            numTrains.append(int(table))
            if x=='2020-12-31':
                break
        if x=='2020-12-31':
            break
    if x=="2020-12-31":
        break

data = {'Year':  year,
'Month': months,
'Day': days,
'Trains': numTrains
}
df = pd.DataFrame(data, columns = ['Year','Month','Day', 'Trains'])
df.to_csv(r'webscraperResultV2.csv')
