# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:18:22 2020

@author: Gokhale

Type hints for multiple arguments and return values
Lots more stuff in the typing module

"""

from typing import Union

def ff(x:int,y:int) -> Union[dict,tuple]:
    if x == 1:
        return {"aa":1}
    if x == 2:
        return ("bb",2)
    
aa=ff(1,2)