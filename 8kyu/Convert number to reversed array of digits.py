"""Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number
within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]"""

# Solution:


def digitize(n):
    n = str(n)
    n = n[::-1]
    result = []
    for digit in n:
        result.append(int(digit))
    return result
