from progress.bar import Bar # sudo pip install progress
import numpy


listy = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        listy.append(i)
print(listy)
x = sum(listy)
print(x)


fib = [1, 2]
x = 0
while x < 4000000:
    fib.append(fib[-2] + fib[-1])
    x = fib[-1]
fib_even = []
for i in fib:
    if i % 2 == 0:
        fib_even.append(i)
x = sum(fib_even)
print(x)


x = time.time()

target = 600851475143

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print (n)

##################
y = time.time()
print("Time it took:", y-x)
print("Time it would take:", (y-x))
"""
"""

time_before = time.time()
##################
listy = []
x = 999
y = 999
condition = True
other_condition = True
while  other_condition:
    condition = True
    y = 999
    while condition:
        number = str(x*y)
        length = len(number)
        if length%2 != 0:
            length -= 1

        length = int(length/2)
        checker = 0
        for i in range(length):
            if number[0+i] == number[-i-1]:
                checker +=1
            else:
                break

        y -=1
        if checker == length:
           listy.append(number)
           condition=False
        if y < 900:
            condition=False

    x -=1
    if x < 900:
        other_condition = False
ass = listy[0]
for i in range(len(listy)):
    if listy[i] < ass:
        ass = listy[i]

print(ass)
print(listy)
##################
time_after = time.time()
print("Time it took:", time_after-time_before)
print("Time it would take:", time_after-time_before)
"""


def prime_lister(x):
    x = x+1
    primeness = True
    primes = [2]
    bar = Bar('Processing', max=x-2, suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')
    for i in range(3, x):
        primeness = True
        for j in primes:
            if numpy.sqrt(i) < j:
                break
            if i == j:
                break
            if i % j == 0:
                primeness = False
        if primeness:
            primes.append(i)
        bar.next()
    bar.finish()
    return primes


"""
x = prime_lister(21)
y = {}
for i in x:
    y[str(i)] = 0
print(y)
print(x)
print(y[str(2)])
for i in range(1,21):
    for j in x:
        if j > i:
            break
        if i % j == 0:
            if (i/j) > (y[str(j)]):
                y[str(j)] = j/i
print(y)
a = 1
for i in y:
    a = a*int(i)*y[i]
print(int(a))
"""
"""
counter = 0
x = prime_lister(21)
print(x)
y = {}
for i in x:
    y[i] = 0
print(y)
for i in range(1, 21):
    for j in x:
        counter = 0
        k = j
        print("Done")
        while True:
            print(i)
            if i % k == 0:
                counter += 1
                if y[j] < counter:
                    y[j] = counter
                    k = k**(counter+1)
                    break
            else:
                break
y[1] = 1
answer = 1
for i in y:
    answer = answer*i
    answer = answer*y[i]

print(y)
print(answer)
"""
"""

def factorer(number):
    x = prime_lister(number, 2)
    y = {}
    for i in x:
        y[i] = 0
    for d in range(2, number):
        for i in x:
            test = True
            counter = 0
            k = d
            print(k, counter, test)
            while test:
                if k % i == 0:
                    k = k / i
                    counter += 1
                    print(k, counter, i)
                else:
                    test = False
                    if y[i] < counter:
                        y[i] = counter

    return y


"""
"""
y = factorer(21)
print(y)
response = 1
for i in y:
    response = response*(i**y[i])
print(response)
"""
"""
import numpy as np

x = np.array([[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]])
y = np.array([[0], [2], [6], [12], [20]])
molester = np.amax(y)
x = x / np.amax(x)
y = y / np.amax(y)
print(x)
print(y)


class NeuralNetwork(object):
    def __init__(self, HiddenLayerSize=5, InputLayerSize=2, OutputLayerSize=1):
        self.HiddenLayerSize = HiddenLayerSize
        self.InputLayerSize = InputLayerSize
        self.OutputLayerSize = OutputLayerSize
        self.W1 = np.random.randn(self.InputLayerSize, self.HiddenLayerSize)
        self.W2 = np.random.randn(self.HiddenLayerSize, self.OutputLayerSize)

    def W1_Values(self):
        return self.W1

    def W2_Values(self):
        return self.W2

    def sigmoid(self, z):
        # Apply sigmoid activation function
        return 1 / (1 + np.exp(-z))

    def sigmoid_prime(self, z):
        return np.exp(-z / ((1 + np.exp(-1)) ** 2))

    def forward(self, X):
        # Propagate inputs through network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat


Baby_G = NeuralNetwork()
print(Baby_G.W1_Values())
print("###################")
un_molested = Baby_G.forward(x)
molested = un_molested * molester
print(molested)
print(np.random.randn(2,10))
"""
"""
x = 0
y = 0

for i in range(101):
    x = x + i
    y = y + i**2

difference = x**2 - y
print(difference)

"""
"""
x = int(input("To what number do you want primes listed: "))

primes = prime_lister(x)


print(primes[10001])
print(primes[10002])
print(primes[10000])


"""

 


def prime_lister(x):
    x = x+1
    primeness = True
    primes = [2]
    for i in range(3, x):
        primeness = True
        for j in primes:
            if numpy.sqrt(i) < j:
                break
            if i == j:
                break
            if i % j == 0:
                primeness = False
        if primeness:
            primes.append(i)
    return primes




