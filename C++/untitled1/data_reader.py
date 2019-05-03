from matplotlib import pyplot as plt


file = open("cmake-build-debug/Data.txt")
data = []
data2 = []

for i in range(16, 201):
    data.append(file.readline(i))


for i in range(len(data)):
    data2.append(float(data[i]))
    print(data2[i])


plt.plot(data2)
plt.show()

