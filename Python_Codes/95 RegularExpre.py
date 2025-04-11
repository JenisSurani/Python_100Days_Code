import re

# Define a regular expression pattern
pattern = r"[A-Z]+ello"

# Match the pattern against a string
text = "Hello, world!,Jello,Tello"

match = re.search(pattern, text) # returns none if pattern not found in the text
# #stops when 1st patterns find


if match: # None is falsy in the python
    print("Match found!")
else:
    print("Match not found.")
    
print(match)

# to find the all occurences


matches = re.findall(pattern, text)
print(matches) # ['Hello', 'Jello', 'Tello']

# # to replace pattern

new_text=re.sub(pattern,"Jenish",text)
print(new_text) # Jenish, world!,Jenish,Jenish


# to extracting  information from a string
txt="he email address is example@example.com."
ptrn= r"\w+@\w+\.\w+"

#\w+ → Matches one or more word characters (letters, numbers, underscore).
# @ → Matches the "@" symbol.
# \w+ → Matches the domain name part before the dot.
# \. → Escaped dot (.) to match a literal period.
# \w+ → Matches the domain extension (e.g., "com", "org").

match=re.search(ptrn,txt)
print(match)

if match:
    email=match.group() #The .group() method extracts the exact substring that matched the pattern.
    print(email)
    
# Author : Jenis Surani
# Topic  : Regular_Expression
# Date   : 03/03/2025