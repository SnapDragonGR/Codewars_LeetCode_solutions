"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns
an array with all of the integer's divisors(except for 1 and the number itself),
from smallest to largest. If the number is prime return the string '(integer) is prime'
(null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Examples:
divisors(12) --> [2, 3, 4, 6]
divisors(25) --> [5]
divisors(13) --> "13 is prime"
"""

# Solution:

def divisors(integer):
    divisors = []
    for i in range(1, integer):
        if integer % i == 0 and i != 1 and i != integer:
            divisors.append(i)
    if not divisors:
        return f'{integer} is prime'
    return divisors
