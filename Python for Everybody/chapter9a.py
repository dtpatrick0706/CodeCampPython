## Collections ##

# A collection is nice because we can put more than one value in it and carry them all around in one convenient package
# We have a bunch of values in a single "variable"
# We do this by having more than one place "in" the variable
# We have ways of finding the different places in the variable

#------------------------------------------------------------------------------------#
## Dictionaries ##
# A dictionary is a "bag" of values, each with its own labael #
# Dictionaries are Python's most powerful data collection
# Dictionaries allow us to do fast database-like operations in Python
# Dictionaries have different names in different languages
    # Associative Arrays - Perl / PHP
    # Properties or Maps or HashMaps - Java
    # Property Bag - C / .Net

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

# Lists index their entries based on the position in the list
# Dictionaries are like bads - no order
# So we index the things we put in the dictionary with a "lookup tag"

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
# { 'money': 12, 'tissues': 75, 'candy': 3 }
print(purse["candy"])
# { 3 }
purse['candy'] = purse['candy'] + 2
print(purse)
# { 'money': 12, 'tissues': 75, 'candy': 5 }

#------------------------------------------------------------------------------------#
## Comparing Lists and Dictionaries ##
# Dictionaries are like lists except that they use keys instead of numbers to look up values 

lst = list()
lst.append(21)
lst.append(183)
print(lst)
# [21, 183]
lst[0] = 23
print(lst)
# [23, 183]

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
# {'course': 182, 'age': 21}
ddd['age']= 23
print(ddd)
# {'course': 182, 'age': 23}

#------------------------------------------------------------------------------------#
## Dictionary Literals (Constants) ##
# Dictionary literals use curly braces and have a list of key : value pairs
# You can make and empty dictionary using empty curly braces

jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)
# {'jan': 100, 'chuck': 1, 'fred': 42}
ooo = {}                # This is the same as dict()
print(ooo)
# { }