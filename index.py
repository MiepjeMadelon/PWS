import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as pyplot
import statistics as st

input_file = "/Users/Yasmin/Documents/pwsprogrammeren/treinstoringen.csv"
data = pd.read_csv('treinstoringen.csv')
df = pd.DataFrame(data)
df = df[['duration_minutes']]
print(df)
