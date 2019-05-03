import numpy as np

print("###################################")
print("#     Neural Network Initiated    #")
print("###################################")
listyX_test = []
listyY_test = []
listyX = []
listyY = []
for i in range(4):
    listyX.append([i, i ** 2])
    listyY.append([i + i ** 2])

for i in range(16,20):
    listyX_test.append([i, i ** 2])
    listyY_test.append([i + i ** 2])


x = np.array(listyX, dtype=float)
y = np.array(listyY, dtype=float)



class Neural_Network:
    def __init__(self, X, Y, learn_rate):
        self.learn_rate = learn_rate
        self.X = X/np.amax(X)
        self.Y = Y/np.amax(Y)
        self.W1 = np.zeros((2, 3))
        self.W2 = np.zeros((3, 1))
        self.Z1 = None
        self.Z2 = None
        self.A1 = None
        self.y_hat = None


    def forward(self):
        self.Z1 = np.dot(self.X, self.W1)
        self.A1 = self.sigmoid(self.Z1)
        self.Z2 = np.dot(self.A1, self.W2)
        self.y_hat = self.sigmoid(self.Z2)
        return self.y_hat

    def sigmoid(self, Z):
        return 1/(1+np.exp(-Z))

    def sigmoid_prime(self, Z):
        return np.exp(-Z)/((1+np.exp(-Z))**2)

    def cost_function(self):
        self.y_hat = self.forward()
        cost = 0.5*(y-self.y_hat)**2
        return cost

    def cost_prime(self):
        self.y_hat = self.forward()
        delta3 = np.multiply(-(y-self.y_hat), self.sigmoid_prime(self.Z2))
        dJdW2 = np.dot(self.A1.T, delta3)

        delta2 = np.multiply(delta3, self.W2.T)*self.sigmoid_prime(self.Z1)
        dJdW1 = np.dot(self.X.T, delta2)

        return dJdW1, dJdW2










Addie = Neural_Network(x, y, 0.1)

Addie.X = x_test
Addie.Y = y_test
print(Addie.forward())
print("##############")
print(Addie.Y)
print(Addie.cost_prime()[0])
print("##############")
print(Addie.cost_prime()[1])

