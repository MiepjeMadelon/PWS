#in this file, we'll look at both the databases and devide the amouth of incidents with the total number of trains.
import numpy as np;
import pandas as pd;
import warnings;
warnings.simplefilter(action='ignore', category=FutureWarning)

allTrainData = pd.read_csv("output_6.csv", header = 0);

numTrains = pd.read_csv("webscraperResultV2.csv", names = ['Year', 'Month', 'Day', 'Trains'], header = 0);

allTrainData = allTrainData.loc[allTrainData['start_year'] == 2019]
numTrains = numTrains.loc[numTrains['Year'] == 2019]
k = 2019
perdaynumDevided = [];
for m in range(12):

    n = m+1
    monthlyTrains = numTrains.loc[numTrains['Month'] == n]
    monthlyData = allTrainData.loc[allTrainData['start_month'] == n]
    for d in range(31):
        e= d+1
        dailyTrains = monthlyTrains.loc[monthlyTrains['Day'] == e]
        dailyData = monthlyData.loc[monthlyData['start_day'] == e]
        lenDailyData = len(dailyData)
        if ((e==29 or e==30 or e==31) and n==2) or (e==31 and (n==4 or n==6 or n==9 or n==11)):
             continue
        else:
            dailyTrains = monthlyTrains.loc[monthlyTrains['Day'] == e]
            numDailyTrains = dailyTrains['Trains'].values[0]
            numcompared = lenDailyData/numDailyTrains
            print('2019' + '-' + str(n) + '-' + str(e))
            print(numcompared)
