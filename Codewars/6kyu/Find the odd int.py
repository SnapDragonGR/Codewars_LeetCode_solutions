"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""


def find_it(seq):
    sorted_seq = sorted(seq)
    count = {}

    for num in sorted_seq:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    for num in count:
        if count[num] % 2 != 0:
            return num