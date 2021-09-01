# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:41:23 2021

@author: User
"""

import pandas as pd
import numpy  as np

# Suppose we have pivot table

df = pd.DataFrame(data={ 'date':['April 1 2001','April 1 2001','April 2 2001','April 2 2001'], 
                         'city':['pune','mumbai','pune','mumbai'],
                        'prop rate':[21234,54324,22311,53211],
                        'tax rate':[12.5, 11.5, 6.4, 6.7]
                        }
                 )



# first column is 'date', 'city' contains pivot fields, and 'prop rate '
# contains data wich is matched with pivot fields

pivoted = df.pivot('date','city','prop rate')

print(df)
print(pivoted)