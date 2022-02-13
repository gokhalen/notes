# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:17:44 2022

@author: User
"""

# Calculates AUC for random classifier
# Point to note is that this random classifier
# Outputs random probabilities
# 

# point corresponding to low threshhold is on the 
# upper right, point for highest threshold 
# is on the lower left

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

nn       = 4096
ycorrect = np.random.choice([0,1],size=(nn,))
yprob    = np.random.random(size=(nn,))
threshhold = np.linspace(0,1.0,101)
tpr_list = []
fpr_list = []
for th in threshhold:
    ypred = (yprob > th).astype('int64')
    cm = confusion_matrix(ycorrect,ypred)
    tn,fp,fn,tp = cm.ravel()
    tpr_list.append(tp/(tp+fn))
    fpr_list.append(fp/(tn+fp))
plt.plot(fpr_list,tpr_list)
plt.plot(tpr_list[0],fpr_list[0],'ro')
plt.plot(tpr_list[-1],fpr_list[-1],'bo')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC Curve for Random Classifier')