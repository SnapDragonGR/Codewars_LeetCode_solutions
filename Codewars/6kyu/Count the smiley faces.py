import re

def count_smileys(arr):
    count = 0
    for smiley in arr:
        if re.search("^[:;][-~]?[D)]$", smiley):
            count += 1
    return count



