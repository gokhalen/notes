# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Pg 305 of Wes McKinney's Python for Data Analysis

import pandas as pd
import numpy as np

people   = pd.DataFrame(np.arange(25).reshape(5, 5),columns=['a', 'b', 'c', 'd', 'e'],index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
key_list = ['one','one','one','two','two']

# so the grouping keys are constructed by 
# (len(index), key list)

# So the key for Joe is (len('Joe'),'one') => (3,'one')
#                Steve is (len('Steve'),'one') => (5,'one')
#                Wes   is (len('Wes'),'one') => (3,'one')

# and so on

grouped = people.groupby([len,key_list])

for key,value in grouped:
    print(key)
    print(value)