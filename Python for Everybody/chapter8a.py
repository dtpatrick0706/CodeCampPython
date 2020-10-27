#### Looking Inside Lists ####

friends = [ 'Joseph', 'Glenn', 'Sally' ]

#------------------------------------------------------------------------------------#
#List Constants

print([1, 24, 76])  # List constants are surrounded by square brackets [] and the elements in the list are seperated by commas
print(['red', 'yellow', 'blue'])
print('red', 24, 98.6)  # A list element can be any Python object - even another list
print([ 1, [5, 6], 7])
print([])  # A list can be empty

#------------------------------------------------------------------------------------#
#Lists and definite loops

friends = [ 'Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year', friend)
print('Done!')

#------------------------------------------------------------------------------------#
#Looking Inside Lists

friends = [ 'Joseph', 'Glenn', 'Sally']
print(friends[1])
#Glenn

#------------------------------------------------------------------------------------#
#Lists are Mutable (can change)

fruit = 'Banana'
fruit[0] = 'b'  # Strings are immutable - we cannot change the contents of a string - we must make a new string to make any change
#Traceback TypeError
x = fruit.lower()
print(x)
#banana
lotto = [2, 14, 26, 41, 63]
print(lotto)
#[2, 14, 26, 41, 63]
lotto[2] = 20  # Lists are mutable - we can change an element of a list using the index operator
print(lotto)
#[2, 12, 28, 41, 63]

#------------------------------------------------------------------------------------#
#How long is a list

greet = 'Hello Bob'
print(len(greet))
# 9
x = [1, 2, 'joe', 99]  # The len() function takes a list as a parameter and returns the number of elements in the list
print(len(x))  # Actually len() tells us the number of elements of any set or sequence (such as a string...)
# 4

#------------------------------------------------------------------------------------#
#Using the range function
print(range(4))  # Using the range function returns a list of numbers that range from zero to one less than the paramete
# [0, 1, 2, 3]
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))  # We can construct an index loop using for and an integer iterator
# 3
print(range(len(friends)))
# [0, 1, 2]

#------------------------------------------------------------------------------------#
# Two different loops

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
for i in range(len(friends)):
    friends = friends[i]
    print('Happy New Year:', friends)