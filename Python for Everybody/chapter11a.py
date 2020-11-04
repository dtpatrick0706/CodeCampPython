## Regular Expressions ##

# In computing, a regular expression, also referred to as "regex" or "regexp", provides a concise and flexible 
# means of matching strings of text, such as particular characters, words, or patterns of characters.
# A regualr expression is written in a formal language that can be interpreted by a regular expression processor.

# Very powerful and quite cryptic
# Fun once you understand them
# Regular expressions are a language unto themselves
# A language of "marker characters" - programming with characters

        # Regular Expression Quick Guide #

#  ^        Mathces the beginning of a line
#  $        Matches the end of the line
#  .        Matches any character
#  \s       Matches whitespace
#  \S       Matches any non-whitespace character
#  *        Repeates a character zero or more times
#  *?       Repeates a character zero or more times (non-greedy)
#  +        Repeats a character one or more times
#  +?       Repeats a chracter one or more times (non-greedy)
#  [aeiou]  Matches a single character in the listed set
#  [^XYZ]   Mathces a single character not in the listed set
# [a-z0-9]  The set of characters can include a range
#  (        Indicates where string extraction is to start
#  )        Indicates where string extraction is to end

#------------------------------------------------------------------------------------#

    # The Regular Expression Module #

# Before you can use regular expressions in your program, you must import the library using "import re"
# You can use re.search() to see if a string matches a regular expression, similiar to using find() method for strings
# You can use re.findall() to extract portions of a string that match your regular expression, 
# similiar to a combination of find() and slicing

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From: ') >= 0:
        print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From: ', line) :
        print(line)

#------------------------------------------------------------------------------------#

    # Using re.search() like startswith() #

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From: ') :
        print(line)

# We fine-tune what is matched by adding special characters to the string

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line) :
        print(line)
