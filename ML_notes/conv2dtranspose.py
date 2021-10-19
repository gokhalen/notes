#https://towardsdatascience.com/types-of-convolutions-in-deep-learning-717013397f4d
#Seems that the input is padded a certain way so that certain output is produced

# https://towardsdatascience.com/understand-transposed-convolutions-and-build-your-own-transposed-convolution-layer-from-scratch-4f5d97b2967

import tensorflow as tf
from tensorflow import keras
import numpy as np

X = np.array([[3, 5, 2, 7], [4, 1, 3, 8], [6, 3, 8, 2], [9, 6, 1, 5]])
X = X.reshape(1,4,4,1)

model_Conv2D = keras.models.Sequential()
layer1 = keras.layers.Conv2D(1,(3,3),strides=(1,1),padding='valid',
                             input_shape=(4,4,1)
                             )
model_Conv2D.add(layer1)
weights = [np.asarray([[[[1]], [[2]], [[1]]], [[[2]], [[1]], [[2]]], [[[1]], [[1]], [[2]]]]), np.asarray([0])]
model_Conv2D.set_weights(weights)
yhat = model_Conv2D.predict(X)
yhat = yhat.reshape(2,2)

# we will now compute this convolution manually
print(f'---- output of model_Conv2d ----')
print('yhat=\n',yhat)
print('weights=\n',weights[0][:,:,0,0])
print('input=\n',X[0,:,:,0])
y00 = 1*3+2*5+1*2 + 2*4+1*1+2*3 + 1*6 + 1*3+2*8
print(f'---- done with model_Conv2d ----')

# other entries can be computed similarly

model_Conv2D_T = keras.models.Sequential()
layer1_T = keras.layers.Conv2DTranspose(1, (3, 3), strides=(1, 1), padding='valid', input_shape=(2, 2, 1))
model_Conv2D_T.add(layer1_T)
weights_T = [np.asarray([[[[1]], [[2]], [[1]]], [[[2]], [[1]], [[2]]], [[[1]], [[1]], [[2]]]]), np.asarray([0])]
model_Conv2D_T.set_weights(weights_T) 
yhat_T = model_Conv2D_T.predict(yhat.reshape(1,2,2,1))

# so basically, as per the explanation given in 
# https://towardsdatascience.com/understand-transposed-convolutions-and-build-your-own-transposed-convolution-layer-from-scratch-4f5d97b2967
# we can build 4 3x3 matrices and combine them to get a 4x4 matrix as shown below

output_T = np.zeros(shape=(4,4),dtype='float64')
m00 = 55*weights[0][:,:,0,0]
m01 = 52*weights[0][:,:,0,0]
m10 = 57*weights[0][:,:,0,0]
m11 = 50*weights[0][:,:,0,0]

output_T[0:3,0:3] += m00
output_T[0:3,1:4] += m01
output_T[1:4,0:3] += m10
output_T[1:4,1:4] += m11

print(f'----output of model_Conv2d_T------')
print('yhat_T=\n',yhat_T[0,:,:,0])
print('output_T=\n',output_T)
print(f'----done with output of model_Conv2d----')