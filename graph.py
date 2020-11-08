#trying to beat Yasmin at this >:)
import numpy as np;
import pandas as pd;
from SDfunction import *
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv('CleanDataNV5.csv')
causeList=df["cause_nl"].tolist()
print(causeList)
numCauses = Counter(causeList)
num50Causes = numCauses.most_common(50)

plt.bar(range(len(numCauses)), list(numCauses.values()))
plt.title("My favorite movies")
plt.ylabel("# of awards")
plt.xticks(range(len(numCauses)), list(numCauses.keys()), rotation = 12)

#plt.savefig('num_causes4.jpg', bbox_inches = 'tight')
#plt.show()
