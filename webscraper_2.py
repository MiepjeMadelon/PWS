import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen



#ik wil kijken of ik x kan opbouwen uit 3 variabelen, het jaar, de maand en dag
#jaar moet van 2018 t/m 2020
#maand moet van 1 t/m 12
#dag moet van 1 t/m 31
#j='2020'
years=['2019', '2020']
for j in years:
    k=str(j)
    for m in range(12):
        n=str(m+1)
        for d in range(31):
            e=str(d+1)
            x = k + '-' + n + '-' + e
            print(x)   #test

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

            html_bytes = page.read()
            html = html_bytes.decode("utf-8")

            start_index = html.find('<td>') + len('<td>')
            end_index = html.find('</td>',start_index)
            table = html[start_index:end_index]

            print(table)
