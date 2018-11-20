#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as pp
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')

db=pd.read_csv('534data.csv')
db.describe()

db.dtypes

sample=db[['age','localization','dx','sex']]

#show graphs of individual features
db['localization'].value_counts().plot(kind='bar')

db['dx'].value_counts().plot(kind='bar')

db['age'].value_counts().plot(kind='bar')

db['sex'].value_counts().plot(kind='bar')

#generate plot with age and dx comparisons
df3 = pd.DataFrame(np.random.randn(1000, 2), columns=['age', 'dx']).cumsum()
df3['sex'] = pd.Series(list(range(len(db))))
df3.plot(x='sex', y='age')

