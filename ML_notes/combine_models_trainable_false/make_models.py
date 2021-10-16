# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 08:52:26 2021

@author: User
"""

from keras import layers
from keras.models import Sequential,Model

import numpy as np

nsamples = 128   # number of samples
nsize    = 64    # length of each sample
train_data   = np.random.random(size=(nsamples,nsize))
train_labels = np.random.choice([0,1],size=(nsamples,))

# make the first model
model1 = Sequential()
model1.add(layers.Dense(32,activation='relu',input_shape=(nsize,)))
model1.add(layers.Dense(1,activation='sigmoid'))
model1.compile(optimizer='rmsprop',loss='binary_crossentropy')
history1 = model1.fit(train_data,train_labels,epochs=16)
model1.save('model1.h5')
model1.summary()

# make the second model
model2 = Sequential()
model2.add(layers.Dense(32,activation='relu',input_shape=(nsize,)))
model2.add(layers.Dense(32,activation='relu',input_shape=(nsize,)))
model2.add(layers.Dense(32,activation='relu',input_shape=(nsize,)))
model2.add(layers.Dense(1,activation='sigmoid'))
model2.compile(optimizer='rmsprop',loss='binary_crossentropy')
history2 = model2.fit(train_data,train_labels,epochs=16)
model2.save('model2.h5')
model2.summary()


