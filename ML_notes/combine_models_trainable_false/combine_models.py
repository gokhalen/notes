# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 09:17:20 2021

@author: User
"""
from keras import layers,Input
from keras.models import Sequential,Model
import keras

import numpy as np

nsamples = 128   # number of samples
nsize    = 64    # length of each sample

train_data   = np.random.random(size=(nsamples,nsize))
train_labels = np.random.choice([0,1],size=(nsamples,))

model1 = keras.models.load_model('model1.h5')
model2 = keras.models.load_model('model2.h5')

# this works
model1.trainable = False
model2.trainable = False

input_data = Input(shape=(nsize,))
predict1   = model1(input_data)
predict2   = model2(input_data)

# this does not work, because predict is probably not a layer
#predict1.trainable = False
#predict2.trainable = False

concat = layers.concatenate([predict1,predict2],axis=-1)
output = layers.Dense(1,activation='sigmoid')(concat)

model = Model(input_data,output)

# this does not work
# model.layers[1].trainable=False
# model.layers[2].trainable=False
# model.layers[-1].trainable=False
model.summary()

model.compile(optimizer='rmsprop',loss='binary_crossentropy')
history = model.fit(train_data,train_labels,epochs=16)
