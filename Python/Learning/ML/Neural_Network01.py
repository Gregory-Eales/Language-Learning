import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x = np.array([[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]], dtype=float)
y = np.array([[0], [2], [6], [12], [20]], dtype=float)
print(x)
print("################")
print(y)


class Neural_Network(object):

    def __init__(self):
        self.InputLayer = 2
        self.HiddenLayer = 3
        self.OutputLayer = 1
        self.W1 = np.random.rand(self.InputLayer, self.HiddenLayer)
        self.W2 = np.random.randn(self.HiddenLayer, self.OutputLayer)

    def forward(self, X):
        self.Z1 = X.dot(self.W1)
        self.A1 = self.Sigmoid(self.Z1)
        self.Z2 = self.A1.dot(self.W2)
        y_hat = self.Sigmoid(self.Z2)
        return y_hat

    def Sigmoid(self, Z):
        a = 1 / (1 + np.exp(-Z))
        return a

    def Sigmoid_Prime(self, Z):
        a_prime = -np.exp(-Z)/(1 + np.exp(-Z))
        return a_prime

    def Cost_Funct(self, y_hat, y):
        self.cost = 0.5*(y_hat - y)**2
        return self.cost

    def cost_prime(self, y_hat, y):
        cost_prime = (y_hat - y)
        return cost_prime






Baby_G = Neural_Network()
print("##################")
print(Baby_G.Cost_Funct(Baby_G.forward(x), y))
plt.plot(Baby_G.forward(x), Baby_G.Cost_Funct(Baby_G.forward(x), y))
#plt.plot(y, Baby_G.Sigmoid(y))
plt.title("Cost Function")
plt.show()
