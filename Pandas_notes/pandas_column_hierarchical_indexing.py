# -*- coding: utf-8 -*-
"""
Nachiket Gokhale
Wes McKinney's  Python for data analysis
page 218
"""

import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
        index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
        columns=[['Ohio', 'Ohio', 'Colorado'],
        ['Green', 'Red', 'Green']])

# don't know how to select all 'Green' columns elegantly
# but can be done via
frame_green=frame[[('Ohio','Green'),('Colorado','Green')]]
print(frame_green)
print(frame.loc[('a',2):('b',1)])