"""
In this little assignment you are given a string of space separated numbers,
and have to return the highest and lowest number.

Examples
Input: "1 2 3 4 5"   =>  Output: "5 1"
Input: "1 2 -3 4 5"  =>  Output: "5 -3"
Input: "1 9 3 4 -5"  =>  Output: "9 -5"
"""

# Solution:

def high_and_low(number):
    numbers = []
    for num in number.split():
        numbers.append(int(num))
    return f"{max(numbers)} {min(numbers)}"
