#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import autocorrelation_plot
from pandas.plotting import parallel_coordinates


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

#autocorrelation
df=pd.DataFrame(np.random.randn(1000, 3), columns=['age', 'sex','dx'])
plt.figure()
autocorrelation_plot(df)

#scatter matrix
scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
with pd.plotting.plot_params.use('x_compat', True):
   .....:     df.age.plot(color='r')
   .....:     df.sex.plot(color='g')
   .....:     df.dx.plot(color='b')
df.plot(subplots=True, figsize=(12, 12));

#parallel coordinates
parallel_coordinates(df, 'dx')
