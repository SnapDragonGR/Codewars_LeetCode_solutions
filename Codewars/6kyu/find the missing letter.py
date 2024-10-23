"""
Find the missing letter

Write a method that takes an array of consecutive (increasing)
letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly
one letter be missing. The length of the array will always be
at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""

# Solution:

def find_missing_letter(chars):
    missing_char = ''
    prev_char = chars[0]

    for char in chars[1:]:
        if ord(char) - ord(prev_char) != 1:
            missing_char += chr(ord(prev_char) + 1)
            break

        prev_char = char

    return missing_char