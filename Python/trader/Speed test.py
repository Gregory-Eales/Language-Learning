import pyspeedtest
from matplotlib import pyplot as plt
import time

test = pyspeedtest.SpeedTest()

data1 = []
data2 = []
x = []

length = 100

for i in range(length):
    print(i, "%")
    data1.append(test.download())



input("Is the dish in place?: ")

for i in range(length):
    print(i, "%")
    data2.append(test.download())


for i in range(length):
    x.append(i)

plt.plot(x, data1, label="Before Dish")
plt.plot(x, data2, label="After Dish")
plt.legend(loc='upper left')
plt.show()




