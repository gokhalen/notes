# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:07:09 2020

@author: Gokhale
"""


ll=["John","Paul",1,2,3]
for item in ll:
    try:
        aa=int(item)
        print("Converted ",item)
        if (aa==3):
            raise RunTimeError("Cannot convert 3")
    except ValueError:
        print("Raising ValueError")
    #except RunTimeError:
    #    print("Except block for RunTimeError")        
    except:
        print("Except branch for unhandled exceptions")
    else:
        print("Else branch executes when no exceptions are thrown")
    finally:
        print("Finally branch executes everytime\n")