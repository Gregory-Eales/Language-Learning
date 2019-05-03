from keras import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from matplotlib import pyplot as plt

"""
model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (5, 5), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
"""

file = open("exchanges - XRP-USD.csv", "r")
data = file.readlines()
y = []
x = []

for i in range(1, len(data)):
    yi = (data[i].split(",")[0])
    x.append(i)
    y.append(float(yi.split('"')[1]))

plt.plot(x, y)
plt.show()
