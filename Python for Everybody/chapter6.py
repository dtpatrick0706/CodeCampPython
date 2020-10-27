fruit = 'banana'
letter = fruit[1]
print(letter)
# a
x = 3
w = fruit[x - 1]
print(w)
# n

fruit = 'banana'
index = 0
while index <len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

word = 'banana'
count = 0
for letter in word:
    if letter =='a':
        count = count + 1
print(count)

word = "bananana"
i = word.find("na")

s = 'Monty Python'
print(s[0:4])
#Mont
print(s[6:7])
#P
print(s[6:20])
#Python
print(s[8:0])
#thon
print(s[:])
#Monty Python

