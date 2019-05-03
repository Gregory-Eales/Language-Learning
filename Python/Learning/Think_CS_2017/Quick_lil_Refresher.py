def basic_function():
    print("This funtion was called")

basic_function()

class BasicClass(object):
    def __init__(self):
        self.string = "This is a basic class"

    def print_method(self):
        print(self.string)
        print("This uses the basic print method")


classy = BasicClass()
