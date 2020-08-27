#trying to make a function of the code from SD.py
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as pyplot
import statistics as st
def calculateSD(database, column):
    column = database[[column]]
    SD = column.std(axis=None, skipna=None, level=None, ddof=1, numeric_only=None)
    return SD*3
