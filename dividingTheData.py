#in this file, we'll look at both the databases and devide the amouth of incidents with the total number of trains.
import numpy as np;
import pandas as pd;
import warnings;
warnings.simplefilter(action='ignore', category=FutureWarning)

allTrainData = pd.read_csv("output_6.csv", header = 0);

numTrains = pd.read_csv("webscraperResultV2.csv", names = ['Year', 'Month', 'Day', 'Trains'], header = 0);

allTrainData = allTrainData.loc[allTrainData['start_year'] == 2019]
k = 2019
perdaynumDevided = [];
for m in range(12):

    n = m+1
    stringn = str(n)

    if n<10:
        stringn = '0' + stringn

    monthlyData = allTrainData.loc[allTrainData['start_month'] == stringn]
    print(monthlyData)
    for d in range(31):
        e= d+1
        stringe = str(e)

        if e<10:
            stringe = '0' + stringe
        dailyData = monthlyData.loc[monthlyData['start_day'] == stringe]
