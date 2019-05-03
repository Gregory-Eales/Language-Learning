"""
import numpy as np

class Neural_Network(object):
    def __init__(self):
        self.InputLayer = 2
        self.HiddenLayer = 3
        self.OutputLayer = 1
        self.W1 = np.random.randn(self.InputLayer, self.HiddenLayer)
        self.W2 = np.random.randn(self.HiddenLayer, self.OutputLayer)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1)
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2)
        yHat = self.sigmoid(self.z2)
        return yHat

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_prime(self, z):
        return np.exp(-z) / ((1 + np.exp(-z)) ** 2)

    def cost_funtion(self, X, y):


    def cost_function_prime(self, X, y):
        self.yHat = self.forward(X)
        delta3 = np.multiply(-(y-self.yHat), self.sigmoid_prime(self.z2))
        djdw2 = np.dot(self.a1.T, delta3)
        delta2 = np.dot(delt3, self.W2.T)*self.sigmoid_prime(self.z2)
        djdw1 = np.dot(X.T, delta2)
        return djdw1, djdw2




X = np.array(([1,1], [2,4], [3,9], [4,16], [5,25], [6,36]), dtype=float)
y = np.array(([1], [3], [6], [10], [15], [21]), dtype=float)
X = X/np.amax(X, axis=0)
y = y/np.amax(y, axis=0)
testvalues = np.arange(-5,5,0.01)
Baby_G = Neural_Network()
Baby_G.W1[1,1] = 5.2
yHat = Baby_G.forward(X)
yHat = yHat*np.amax(y, axis=0)
cost = 0.5*((y-yHat)**2)
"""