#### Working with Lists Pt.2 ####

#Concatenating lists using +

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b                  # We can create a new list by adding two existing lists together
print(c)
# [1, 2, 3, 4, 5, 6]
print(a)
# [1, 2, 3]

#------------------------------------------------------------------------------------#
#Lists can be sliced using :

t = [9, 41, 12, 3, 74, 15]
t[1:3]
# [41, 12]
t[:4]                      # Remeber: Just like in strings the second number is "up to but not including"
# [9, 41, 12, 3]
t[3:]
# [3, 74, 15]
t[:]
# [9, 41, 12, 3, 74, 15]

#------------------------------------------------------------------------------------#
#Building a List from Scrach

stuff = list()             # We can create and empty list
stuff.append('book')       # Then we add elements using the append method
stuff.append(99)
print(stuff)
# ['book', 99]             # The list stays in order
stuff.append('cookie')
print(stuff)
# ['book', 99, 'cookie]    # New elements are added at the end of the list

#------------------------------------------------------------------------------------#
#Is Something in a List

some = [1, 9, 21, 10, 16]  # Python provides two operators that let you check if an item is in a list
9 in some
# True                     # These are logical operators that return True or False
15 in some
# False                    # They do not modify the list
20 not in some
# True

#------------------------------------------------------------------------------------#
# Lists are in Order

friends = ['Joseph', 'Glenn', 'Sally']         # A list can hold many items and keeps those items in order until we do something to change the order
friends.sort()                                 # A list can be sorted (i.e., change its order)
print(friends)                                 # The sort methos (unlike in strings) means "sort yourself"
# ['Glenn', 'Joseph', 'Sally']

#------------------------------------------------------------------------------------#
# Same Program Different Ways

# Way number 1
total = 0
count = 0
while True :
    inp = input('Enter a number: ')
    if inp =='done' :
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average: ', average)

# Way number 2
numlist = list()
while True : 
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: '), average
