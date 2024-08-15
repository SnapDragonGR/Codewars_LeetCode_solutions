"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
"""

# Solution:


def maps(a):
    result = []
    for num in a:
        num *= 2
        result.append(num)
    return result
