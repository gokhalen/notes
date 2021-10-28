# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:12:25 2021

@author: User
"""

# https://analyticsindiamag.com/a-guide-to-bayesian-statistics-in-python-for-beginners/

# For example, suppose we have 2 buckets A and B. 
# In bucket A we have 30 blue balls and 10 yellow balls,
# while in bucket B we have 20 blue and 20 yellow balls.
# We are required to choose one ball.
# We have picked a blue ball. What is the chance that we have picked 
# it from bucket A?

# simple solution:
# There are 50 blue balls. 30 in bucket A and 20 in bucket B
# So, given that we have picked a blue ball the probability 
# we have picked it from A is 30/50 = 0.6

# Numpy solution
# priors - P(A), P(B)
# likelihood - P(Blueball|A) P(Blueball|B)
# P(A|Blueball)*P(Blueball) = P(Blueball|A)*P(A)   
# P(A|Blueball) = (3/4)*(0.5)/(5/8) = 0.6

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hypos = 'bucket a','bucket b'
probs = 1/2 , 1/2
prior = pd.Series(probs,hypos) # P(A) and P(B)
likelihood = 3/4,1/2           # P(Blueball|A) and P(Blueball|B)

# unnormalized
unnorm = prior*likelihood  # P(Blueball|A)*P(A) and P(Blueball|B)*P(B)  

prob_data = unnorm.sum()  # P(Blueball|A)*P(A) + P(Blueball|B)*P(B)

posterior = unnorm / prob_data

print(posterior)
print('-'*80)

# Typo corrected
# Now suppose a similar situation as given in the above problem,
# putting back the previous lifted ball and choosing a ball from the buckets
# and it is a yellow ball. Now, what is the probability
# that both times we chose bucket A to pick the ball?

# prior1 = posterior   (we have picked Blue ball bucket A, we have picked Blueball from B)
prior1 = posterior
likelihood1 = 1/4,1/2  #P(Yellow|A) and P(Yellow|B)
unnorm1 = prior1*likelihood1
prob_data1 = unnorm1.sum()

posterior1 = unnorm1/prob_data1
print(posterior1)

