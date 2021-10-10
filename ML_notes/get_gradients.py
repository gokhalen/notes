# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 12:42:19 2021

@author: User
"""

# Getting layer weights and gradients
# https://keras.io/getting_started/intro_to_keras_for_researchers/

import tensorflow as tf
from keras import layers, Input
from keras.models import Sequential,Model
import numpy as np

nveclength = 64 
nunits     = 16
nsamples   = 32

x_train = np.random.random(size=(nsamples,nveclength))
y_train = np.random.choice([0,1],size=(nsamples,))

# 
x      = Input(shape=(nveclength,),dtype='int64')
layer1 = layers.Dense(nunits,activation='linear')(x)
layer2 = layers.Dense(nunits,activation='relu')(layer1)
output = layers.Dense(1,activation='sigmoid')(layer2)
model  = Model(x,output)
model.summary()
model.compile(loss='mse',optimizer='rmsprop')
model.fit(x_train,y_train,epochs=10,batch_size=8)

print('-'*80)
print('-'*80)
print('-'*80)


seq_model = Sequential()
seq_model.add(layers.Dense(nunits,activation='linear',input_shape=(nveclength,)))
seq_model.add(layers.Dense(nunits,activation='relu'))
seq_model.add(layers.Dense(1,activation='sigmoid'))
seq_model.summary()
seq_model.compile(loss='mse',optimizer='rmsprop')
seq_model.fit(x_train,y_train,epochs=10,batch_size=8)   


# to get weights, the following works both for sequential and functional models
#for layer in model.layers:
#    print(layer.trainable_weights)
#for layer in seq_model.layers:
#    print(layer.trainable_weights)

# now gradients
layer1  = layers.Dense(nunits,activation='linear')
layer2  = layers.Dense(nunits,activation='relu')
output  = layers.Dense(1,activation='sigmoid')
loss_fn = tf.keras.losses.MeanSquaredError()
with tf.GradientTape() as tape:
    logits1 = layer1(x_train)
    logits2 = layer2(logits1)
    logits3 = output(logits2)
    loss    = loss_fn(y_train.reshape((-1,1)),logits3)
    
gradients = tape.gradient(loss,layer1.trainable_weights)

# gradients is a list
# gradients[0] apparently contains all the weights connecting the input
# to layer1. There are nveclength*nunits here
# gradient[1] is the gradient wrt weights associated with the bias 
print(f'{gradients=}')