import tensorflow as tf
import numpy as np


ann = tf.keras.models.Sequential()

# Adding the input layer and the first hidden layer

# need to explicitly specify the shape of the input layer in order to plot 
# the ann using plot_model
ann.add(tf.keras.Input(shape=(12,)))
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

# visualize the ann
tf.keras.utils.plot_model(ann, to_file='model.png', show_shapes=True, 
                          show_layer_names=True, rankdir='TB',
                          expand_nested=False, dpi=96
                          )

