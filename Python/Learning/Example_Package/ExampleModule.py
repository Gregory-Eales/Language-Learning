class Example:
    def __init__(self):
        self.example = 696969

    def printer(self):
        return self.example


class Database:
    pass


database = None


def initialize_database():
    global database
    database = Database()

def string_formatter(string, formatter=None):
    class Default_Formatter:
        def format(self, string):
            return str(string).title()
    if not formatter:
        formatter = Default_Formatter()

    return formatter.format(string)
"""
hello_string = "hello world, how are you today?"
print(string_formatter(hello_string))
"""




