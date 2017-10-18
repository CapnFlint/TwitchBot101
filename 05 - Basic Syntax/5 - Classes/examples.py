'''
Classes
'''

class MyClass():

    def __init__(self, param1):
        self.classVar = param1

    def print_var(self):
        print self.classVar

    def get_var(self):
        return self.classVar

    def set_var(self, value):
        self.classVar = value

myObject = MyClass("Hello")
myObject.print_var()
myObject.set_var("World")
print myObject.get_var()
