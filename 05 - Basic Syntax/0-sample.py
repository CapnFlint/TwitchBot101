#!/usr/bin/env python27

'''
This is a multiline comment
'''

# These are imports
import logging

# Colon (:) signifies the start of a block!
def globalFunction(myVar):

    # Some operators
    message = "Hello " + myVar + "!"

    # Built in function
    # This works the same:
    #   print(message)
    print message

# This is a class
class MyClass():

    # prototype function
    def __init__(self, myVar):
        self.myClassVar = myVar

    # class function (method)
    def updateVar(self, newVar):
        print "Updating class variable..."

        self.myClassVar = newVar

    def read_var(self):

        # return statement
        return self.myClassVar

    def callGlobalFunc(self):
        globalFunction(self.myClassVar)


globalFunction("World")
myObject = MyClass("Twitch Chat")

print "Variable contains: " + myObject.read_var()

myObject.callGlobalFunc()
myObject.updateVar("Everyone")
myObject.callGlobalFunc()
