import matplotlib.pyplot as plt

# history is defined by the fit function
# history=cnn.fit(x = training_set, validation_data = test_set, epochs = 25)


loss_values = history.history['loss']

# we can also do
# accuracy_values = history.history['accuracy']

epochs = range(1, len(loss_values)+1)
plt.plot(epochs, loss_values, label='Training Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# better still
# plot 
for ikey in history.history.keys():
    plt.figure(ikey)
    data   = history.history[ikey]
    epochs = range(1,len(data)+1)
    plt.plot(epochs,data)
    plt.title(ikey)
    plt.xlabel('epochs')
    plt.ylabel(ikey)
