"""
Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

# Solution:

def reverse_words(text):
    rev_text = ''.join(char for char in reversed(text))
    split_rev = rev_text.split(' ')
    split_rev.reverse()
    output = ' '.join(split_rev)
    return output
