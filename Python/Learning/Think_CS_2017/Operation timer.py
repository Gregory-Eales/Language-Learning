import time
import numpy

time1 = time.time()

for i in range(10000000):
    10000000000**0.5

time2 = time.time()

print(time2-time1)

time1 = time.time()

for i in range(10000000):
    numpy.sqrt(10000000000)

time2 = time.time()

print(time2 - time1)
