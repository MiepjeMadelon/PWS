import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = 'https://www.rijdendetreinen.nl/treinarchief/2020-11-24/utrecht-centraal'
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
