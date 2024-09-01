import re

str = "an example word:cat!!"

#The re.search() method, returns a match object or None
#r stipulates a raw string meaning that backslashes do not have any special meaning.
match = re.search(r'word', str)  #Searching for the the pattern word followed by a 3 letter word.

#If statement to test if the match succeeded
if match:
    print("found", match.group())       #match.group() method returns the exact word found.
else:
    print("No match")