'''
Functions
'''

globalVar = "A Global Variable"

def my_function(var1, var2 = "default value"):
    global globalVar
    localVar = "A Local Variable"

    print "Called my_function!"

    return True

# basic function call
my_function("foo", "bar")

# assign return value to var
result = my_function("foo", "bar")

# explicit parameter allocation
my_function(var2="bar",var1="foo")

# class function call
MyClass.classFunction()
