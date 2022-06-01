# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:27:35 2022

@author: Nachiket Gokhale
"""
import numpy as np
from sklearn.decomposition import PCA

# non-centered data
m = 10  # data points 
n = 4   # features
X = np.random.random((m*n)).reshape(m,n)

pca = PCA(2)
pca.fit(X)
X2D = pca.fit_transform(X)

X2D_manual = (X-np.mean(X,axis=0))@pca.components_.T


# Recovery
X_rec        = pca.inverse_transform(X2D)
means        = np.mean(X,axis=0)
X_rec_manual = X2D_manual@pca.components_ + means

print(np.linalg.norm(X_rec-X_rec_manual))
