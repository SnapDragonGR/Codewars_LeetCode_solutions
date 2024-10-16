"""
There is an array with some numbers. All numbers are equal except for one.
Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

"""

# Solution:

def find_uniq(arr):
    num_count = {}

    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    for num, count in num_count.items():
        if count == 1:
            return num
