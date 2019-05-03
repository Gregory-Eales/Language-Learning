# This section is on data structures
# and how to correctly handle data with objects
from collections import namedtuple

Stock = namedtuple("Stock", "Symbol Current High Low")
Microsoft = Stock("MSFT", 100, 120, 80)
print(Microsoft)
# This shows how to make named tuples so later
# each data value is understandable
Stocks = {"MSFT": (100, 120, 99), "GOOGL": (100, 200, 300)}
print(Stocks.get("FART"))
from collections import defaultdict


def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies
print(letter_frequency("Arianna"))

class particle:
    def __init__(self, weight, charge=None):
        self.weight = weight
        self.charge = charge

Neutron = particle(1)

Contents = "This is some pretty hot file contents"

def no_args():
    pass

def args(name="David", age=21, weight=200, height=6.0, skin_color="White"):
    return name, age, weight, height, skin_color
print(args(weight=500, name="Alex"))
listy = ["a","b","c","d","e","f","g"]
for i,v in enumerate(listy):
    (i+1,v)

class Employee:
    def __init__(self, first, last):
        self.last = last
        self.first = first
        self.email = first+"."+last+"@gmail.com"

GaryVee = Employee("Gary", "Vanderchuck")
print(GaryVee.email)


print("{},,,, {}".format("hello", "goodbye"))


class Generic:
    def __init__(self, laugh=True, lie=False):
        self.laugh = laugh
        self.lie = lie

Arianna = Generic()
print(Arianna.laugh)
print(Arianna.lie)
Arianna.laugh = 50
print(Arianna.laugh)

def sick_function():
    print("The function was called")
sick_function.descriptons = 32


class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = str(first)+str(last)+"@HoeMail.com"

GaryVee = Contact("Gary", "Vanderchuck")
print(GaryVee.email)

