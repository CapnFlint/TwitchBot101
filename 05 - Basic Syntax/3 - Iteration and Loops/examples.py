'''
Iteration and Loops
'''

# If-Else
a = 2
if a == 1:
    print "a is 1"
elif a == 2:
    print "a is 2"
else:
    print "a isn't 1 or 2"

# for
myList = [1,2,3,4,5]
for element in myList:
    print element

# while
count = 10
while count > 0:
    print count
    count = count - 1
print "Blastoff!"

# Break
haystack = [1,4,6,8,9]
needle = 6
pos = 0
while pos < len(haystack):
    if haystack[pos] == needle:
        break
    pos += 1
print "Needle found at position: " + str(pos)

# Continue
myList = [1,1,0,1,0,0,0,1,0,1]
count = 0
for item in myList:
    if item == 0:
        continue
    count += 1
print "Found: " + str(count)
