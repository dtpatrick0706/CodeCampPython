## Tuples ##
# Tuples are like Lists #
# Tuples are another kind of sequence that functions much like a list - they have elements which are indexed starting at 0

x = ('Glenn', 'Sally', 'Joseph')  # initialized using ()
print(x[2])
# Joseph
y = (1, 9, 2)
# (1, 9, 2)
print(max(y))
# (9)

#------------------------------------------------------------------------------------#

# but.... Tuples are "immutable" #
# Unlike a list, once  you create a tuple, you cannot alter its contents - similiar to a string

x = [9, 8, 7]
x[2] = 6
print(x)
# [9, 8, 6]

z = (5, 4, 3)
z[2] = 0
# Traceback : 'tuple'

#------------------------------------------------------------------------------------#

# Not to do #
# Tuples are meant to be used and disgarded for quick tasks
# Tuples are very efficient, and essentially limited lists
x = (3, 2, 1)
x.sort()
x.append()
x.reverse()
# x....

#------------------------------------------------------------------------------------#

# Tuples are more efficient #
# Since Python does not have to build structures to be modifiable, they are similiar and more efficient in terms of memory use and performance than lists
# So in a program when you are making "temporary variables" you prefer tuples over lists

#------------------------------------------------------------------------------------#

# Tuples and Assignments #
# We can also put a tuple on the left-handed side of an assignment statement
# We can even omit the parentheses

(x,y) = (4, 'fred')
print(y)
# fred
(a,b) = (99,98)
print(a)
# 99

#------------------------------------------------------------------------------------#

# Tuples and Dictionaries #
# The items() method in dictionaries returns a list of(key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)
# csev 2
# cwen 4
tups = d.items()
print(tups)
# dict_items([('csev', 2), ('cwen', 4)])

#------------------------------------------------------------------------------------#

# Tuples are Comparable
# The comparison operations work with tuples and other sequences. If the first item is equal, Python goes on to the next element, and so on until it finds elements that differ
# It only scans until it has a diffinitive answer and then it stops scanning

(0, 1, 2) < (5, 1, 2)
# True
(0, 1, 2000000) < (0, 3, 4)
# True
('Jones', 'Sally') < ('Jones', 'Sam')
# True
('Jones', 'Sally') > ('Adams', 'Sam')
# True
