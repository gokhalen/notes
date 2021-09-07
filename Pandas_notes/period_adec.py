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

# now from high frequency to low freq
# this defines a period of one month
p = pd.Period('Aug-2007','M')
# now we are getting a bigger period from p
# we are asking in which year period ending in June
# does Aug-2007 lie
# the answer is July-1-2007 to Jun-30-2008
p2 = p.asfreq('A-JUN')
# we can check the start and end dates
print(p2.asfreq('D',how='start'))
print(p2.asfreq('D',how='end'))
