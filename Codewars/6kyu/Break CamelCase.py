"""
Complete the solution so that the function will break up camel casing, using a space between words.
Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""

# Solution:

import re

def solution(s):
    s = re.split(r'(?=[A-Z])', s)
    return ' '.join(word for word in s)
