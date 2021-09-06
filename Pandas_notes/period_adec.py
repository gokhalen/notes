# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 17:23:12 2021

@author: User
"""

import pandas as pd
import numpy as np

# Table 11-4 in Ws McInney's Python for data analysis
#  Pg 351 Period frequency conversion


# defines a period whose 
# first date is the 2007-01-31
# last date is the 2007-12-31
p = pd.Period('2007',freq='A-DEC')
# check
print(p.asfreq('D',how='start'))
print(p.asfreq('D',how='end'))

# similarly
# first date is the 2006-08-1
# last date is the 2007-07-31
p = pd.Period('2007',freq='A-JUL')
print(p.asfreq('D',how='start'))
print(p.asfreq('D',how='end'))