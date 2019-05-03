"""
from Example_Package import ExampleModule as E
from Notebook_CaseStudy import Notebook as nb

class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        distance = math.sqrt(
            (self.x**2 + self.y**2)
        )
        return distance
p = Point(3, 4)
print(p.distance())
"""
"""
hello = "hello world, how are you today?"
example = E.string_formatter(hello)
print(example)


N = nb.NoteBook()
N.notes("Yup")
N.notes("Wowza")
print(N.note[2].memo)
"""

class User:

    user_data = []

    def __init__(self, first, last, phone, salary, password):
        self.first = first
        self.last = last
        self.phone = phone
        self.salary = salary
        self.email = first+last+"@company.com"
        self.password = password
        self.status = None

    def login_user(self, password):
        if password == self.password:
            self.status = "online"

    def logout_user(self):
        self.status = "offline"


x = {"0001":["Gregory", "Eales"]}
print(x["0001"])

while True:
    print("Options: New User - 0, Login -")


















