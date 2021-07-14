# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:48:41 2021

@author: aa
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

xvals = np.linspace(-10,10,1024)

def plotarr(xx,yy,leg,fname):
    plt.figure()
    plt.plot(xx,yy,linewidth='4')
    plt.grid(True,which='both',linewidth='2')
    plt.xlabel('input',fontsize=18)
    plt.ylabel('output',fontsize=18)
    plt.legend([leg],fontsize=18)
    plt.savefig(fname,bbox_inches='tight')


# plot tanh
yvals = tf.keras.backend.tanh(xvals)
plotarr(xvals,yvals,'tanh','tanh.png')
# plot logistic
yvals = tf.keras.backend.sigmoid(xvals)
plotarr(xvals,yvals,'logistic','logistic.png')
# plot softplus
yvals = tf.keras.backend.softplus(xvals)
plotarr(xvals,yvals,'softplus','softplus.png')
# twisted tanh
yvals = tf.keras.backend.tanh(xvals) + 0.01*xvals
plotarr(xvals,yvals,'twisted tanh','twistedtanh.png')
# max softplus
yvals = np.minimum(tf.keras.backend.softplus(xvals),1.0)
plotarr(xvals,yvals,'min(softplus,1)','minsoftplus.png')
