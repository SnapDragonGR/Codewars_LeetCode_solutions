"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second
character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

# Solution:

def solution(s):
    output = []
    count = 0
    if len(s) % 2 == 0:
        for i in range(0, len(s), 2):
            output.append(s[i:i + 2])
        return output
    else:
        s += '_'
        for i in range(0, len(s), 2):
            output.append(s[i:i + 2])
        return output
