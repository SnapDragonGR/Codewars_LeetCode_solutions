"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""

# Solution:

import re

def validate_pin(pin):
    if re.fullmatch(r'\b\d{4}\b', pin) or re.fullmatch(r'\b\d{6}\b', pin):
        return True
    else:
        return False
