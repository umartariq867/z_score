# -*- coding: utf-8 -*-
"""zscore.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/161sBWMR7axegCWlLDQV7JpcotXIQmcJZ
"""

import pandas as pd
from scipy import stats
import numpy as np

dataset1 = pd.read_csv('/content/bhp.csv')

print(dataset1.head())
print(dataset1.columns)
col = dataset1.columns
z = stats.zscore(dataset1.iloc[:,2:])

print(z)
print(np.where(z > 3))

for i in range(2,len(col)):
       p = np.percentile(dataset1.iloc[:,i], 75)
       y = dataset1[col[i]]
       # print(p)
       for j in range(len(y)):
          if y[j] > p:
              y = y.replace(y[j],p)
       dataset1[col[i]]=y
       # print(dataset1)

       p = np.percentile(dataset1[col[i]], 10)
       # print(value)
       for j in range(len(y)):
          if y[j] < p:
                 y = y.replace(y[j], p)
       dataset1[col[i]] = y

z = stats.zscore(dataset1.iloc[:,2:])

print(z)
print(np.where(z > 3))
print(dataset1.head())