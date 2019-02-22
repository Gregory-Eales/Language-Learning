import math 

# basic class syntax
class MyClass(object):
	pass

a = MyClass()
b = MyClass()

print(a)
print(b)


class Point():
	""" Represents a 2-D point"""

	def __init__(self, x=0, y=0):
		""" initialize the point """
		self.x = x
		self.y = y

	def reset(self):
		""" set the point back to the origin """
		self.x = 0
		self.y = 0

	def move(self, x, y):
		""" moves the point to x, y """
		self.x = x
		self.y = y

	def calculate_distance(self, other_point):
		""" calculates the distance between 
		the point and another """
		deltaX = (self.x - other_point.x)**2
		deltaY = (self.y - other_point.y)**2
		return math.sqrt(deltaY + deltaX)

p1 = Point(3, 4)
p2 = Point()
distance = p1.calculate_distance(p2)
print("The distance between the points is:", distance, "units")












