import numpy as np
from matplotlib import pyplot as plt

X = np.array(([3, 5], [5, 1], [10, 2]))
X = X / np.max(X)
y = np.array(([75], [82], [93]))
y = y / np.max(y)


class Neural_Network(object):
    def __init__(self):
        self.input_layer = 2
        self.hidden_layer = 3
        self.output_layer = 1

        self.w1 = np.random.rand(self.input_layer, self.hidden_layer)
        self.w2 = np.random.rand(self.hidden_layer, self.output_layer)

    def forward(self, X):
        self.z1 = np.dot(X, self.w1)
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.w2)
        self.y_hat = self.sigmoid(self.z2)
        return self.y_hat

    def cost_function(self, X, y):
        self.y_hat = self.forward(X)
        J = sum((self.y_hat - y) ** 2)

    def cost_function_prime(self, X, y):
        self.y_hat = self.forward(X)
        delta3 = np.multiply(-(y - self.y_hat), self.sigmoid_prime(self.z2))
        djdw2 = np.dot(self.a1.T, delta3)

        delta2 = np.dot(delta3, self.w2.T) * self.sigmoid_prime(self.z1)
        djdw1 = np.dot(X.T, delta2)

        return djdw1, djdw2

    def sigmoid(self, z):
        sigmoid = 1 / (1 + np.exp(-z))
        return sigmoid

    def sigmoid_prime(self, z):
        sig_prime = np.exp(-z) / ((1 + np.exp(-z)) ** 2)
        return sig_prime

    def get_params(self):
        params = np.concatenate((self.w1.ravel(), self.w2.ravel()))
        return params

    def set_params(self, params):
        w1_start = 0
        w1_end = self.hidden_layer * self.output_layer
        self.w1 = np.reshape(params[w1_start:w1_end], (self.input_layer, self.hidden_layer))
        w2_end = w1_end + self.output_layer * self.hidden_layer
        self.w2 = np.reshape(params[w1_end:w2_end], (self.hidden_layer, self.output_layer))

    def compute_gradient(self, X, y):
        dJdW1, dJdW2 = self.cost_function(X, y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))

def compute_numrical_gradient(N, X, y):
    paramsInitial = N.getParams()
    numgrad = np.zeros(paramsInitial.shape)
    purturb = np.zeros(paramsInitial.shape)
    e = 1e-4

    for p in range(len(paramsInitial)):
        purturb[p] = e
        N.set_params(peramsInitial + purturb)
        loss2 = N.cost_function(X, y)

Baby_G = Neural_Network()
