# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:01:54 2021

@author: User
"""

# From Wes McKinney's book - Python for Data Analysis, Wrangling 
# pg. 344

# It is not clear how mean() works when resampling

import pandas as pd
import numpy as np
from pandas.tseries.offsets import Day,MonthEnd

ts = pd.Series(np.random.randn(20),index = pd.date_range('1/15/2000', periods=20, freq='4d'))
offset = MonthEnd()

ts_resample_mean = ts.resample('M').mean()
print(ts_resample_mean)

# first entry
print(ts[0:5].mean())
# second entry
print(ts[5:12].mean())
# third entry
print(ts[12:].mean())
