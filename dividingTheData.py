#in this file, we'll look at both the databases and devide the amouth of incidents with the total number of trains.
import numpy as np;
import pandas as pd;
import warnings;
warnings.simplefilter(action='ignore', category=FutureWarning)

allTrainData = pd.read_csv("output_6.csv", header = 0);

numTrains = pd.read_csv("webscraperResultV2.csv", names = ['Year', 'Month', 'Day', 'Trains'], header = 0);

allTrainData = allTrainData.loc[allTrainData['start_year'] == 2019]

rdtLines = allTrainData['rdt_lines'].tolist()
j = 0
indexUtrechtData = []
for i in rdtLines:
    try:
        if 'Utrecht Centraal' in i:
            indexUtrechtData.append(j)
    except Exception as e:
        pass
    j = j+1

#UtrechtData = allTrainData[allTrainData.id in indexUtrechtData]


k = 2019
months = [];
days = [];
numDataTotal = []; #DATA
numDataUtrechtCentraal = [];#DATA
numTrainsUtrechtCentraal = [];#TRAINS
perdaynumDevidedTotal = [];#BOTH
for m in range(12):
    n = m+1
    monthlyTrains = numTrains.loc[numTrains['Month'] == n]#TRAINS
    monthlyData = allTrainData.loc[allTrainData['start_month'] == n]#DATA
    for d in range(31):
        e= d+1
        dailyData = monthlyData.loc[monthlyData['start_day'] == e]#DATA
        lenDailyData = len(dailyData)#DATA
        if ((e==29 or e==30 or e==31) and n==2) or (e==31 and (n==4 or n==6 or n==9 or n==11)):
             continue
        else:
            dailyTrains = monthlyTrains.loc[monthlyTrains['Day'] == e]#TRAINS
            numDailyTrains = dailyTrains['Trains'].values[0]#TRAINS
            numcompared = lenDailyData/numDailyTrains#BOTH
            #print('2019' + '-' + str(n) + '-' + str(e))
            #print(numcompared)
            months.append(n)
            days.append(e)
            numDataTotal.append(lenDailyData)
            #This code is not yet correct, it now checks for all rows that day

            try:
                if 'Utrecht Centraal' in dailyData['rdt_lines'].values[0]:
                    pass
                else:
                    #print('nope')
                    pass
            except Exception as e:
                if True:
                    #print('NOPE')
                    pass
