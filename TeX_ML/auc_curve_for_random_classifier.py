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
prec_list = []
rec_list  = []

# plot Auc Curve
for th in threshhold:
    ypred = (yprob > th).astype('int64')
    cm = confusion_matrix(ycorrect,ypred)
    tn,fp,fn,tp = cm.ravel()
    
    
    tpr_list.append(tp/(tp+fn))
    fpr_list.append(fp/(tn+fp))
    
    prec_list.append(tp/(tp+fp))
    rec_list.append(tp/(tp+fn))
    

# Plot Auc Curve    
plt.figure()
plt.plot(fpr_list,tpr_list)
plt.plot(tpr_list[0],fpr_list[0],'ro')
plt.plot(tpr_list[-1],fpr_list[-1],'bo')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC Curve for Random Classifier')

# Plot 
# this plot is a bit tricky to explain
# 1) Our output dataset is balanced - same number 
#    of 0's as 1's
# 2) Precision curve:  TP/(TP+FP) = TP/Pred +ve
#    As threshold increases, the number of predicted
#    positives drops, i.e.  denominator drops.
#    As the dataset is balanced about half of these
#    predicted positives are correct. So precision
#    howers at around 0.5
# 3) Recall: TP/(TP+FN) = TP/Actual +ve
#    Here, the denominator is constant because the 
#    number of actual positives does not change
#    However, the TP keeps dropping beaause 
#    the number of predicted positives drops as
#    the threshold is raised.  Hence recall drops
#    as threshold is raised.

plt.figure()
plt.plot(threshhold,prec_list,'b-',label='precision')
plt.plot(threshhold,rec_list,'r-',label='recall')
plt.xlabel('threshhold')
plt.ylabel('precision/recall')
plt.title('Pr Vs Recall')
plt.legend()