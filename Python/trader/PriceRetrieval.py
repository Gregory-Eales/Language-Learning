import poloniex
import time
from matplotlib import pyplot


apiKey = "8LS264B7-148VJHAV-1EKLVZF0-JD5WTLPS"
secret = "5f1dc4c23f41121a9031a04da5c7fce45be02475c3d2106a2f8494f2353762c0caf34407f9846cdb87bf75e8393add5dbc0469a984e139c1d6015eaeb7d99727"
polo = poloniex.Poloniex(key=apiKey, secret=secret)
data = polo.returnOrderBook('BTC_XRP', 1000000000)
print(data)


asks = data['asks']
x = []
y = []
z = []
s = []
for i in range(len(asks)):
    z.append(i)

for i in asks:
    y.append(float(i[0]))
    x.append(float(i[1]))
    s.append(float(i[0])*float(i[1]))

pyplot.hist(x, rwidth=0.1)
pyplot.show()
pyplot.plot(y, z)
pyplot.show()
pyplot.scatter(y, x)
pyplot.show()
