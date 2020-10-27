
stuff = 'Hello\nWorld'
stuff
print(stuff)

stuff = 'X\nY'
print(stuff)
len(stuff)
#3

# Chapter 7 part 2

xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

# - a file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
# - We can use the for statement to iterate through a sequence
# - Remember a sequence is an ordered set

#------------------------------------------------------------------------------------#
fhand = open('mboc.txt')  # open a file read-only
count = 0
for line in fhand:  # Use a for loop to read each line
    count = count + 1  # Count the lines and print out the number of lines
print('Line Count:', count)

#------------------------------------------------------------------------------------#
fhand = open('mbox-short.txt')
inp = fhand.read()  #We can read the whole file (newlines and all) into a single string
print(len(inp))
#94626
print(inp[:20])

#------------------------------------------------------------------------------------#
fhand = open('mbox-short.txt')
for line in fhand:
    if line.statement('From:'):  #We can put if statements in our for loop to only print lines that meet some criteria
        print(line)

#------------------------------------------------------------------------------------#
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()  #We can strip the whitespace from the right-hand side of the string using rstip() from the string library
    if line.startswith('From:'):  #The newline is considered "white space" and is strippped
        print(line)

#------------------------------------------------------------------------------------#
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue  #We can conveniently skip a line by using the continue statement
        print(line)

#------------------------------------------------------------------------------------#
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:  #We can look for a string anywhere in a line as our selection criteria
        continue
    print(line)

#------------------------------------------------------------------------------------#
fname = input('Enter the file name: ')  #Make the filename be an input statement
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)

#------------------------------------------------------------------------------------#
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
