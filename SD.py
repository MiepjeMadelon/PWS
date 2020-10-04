import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as pyplot
import statistics as st

#database toevoegen
input_file = '/Users/Yasmin/Documents/pwsprogrammeren/treinstoringen.csv'
data = pd.read_csv('treinstoringen.csv')
#dataframe df aanmaken
df = pd.DataFrame(data)
#column duration_minutes pakken
df = df[['duration_minutes']]
#proberen de standard deviaton uit te rekenen en falen
SD = df.std(axis=None, skipna=None, level=None, ddof=1, numeric_only=None)
#de resultaten uitprinten zodat ik een leuke error krijg 😭
print(SD)
print(" hello")
