"""
Complete the method/function so that it converts dash/underscore
delimited words into camel casing. The first word within the output
should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

# Solution:

def to_camel_case(text):
    output = []
    skip_next = False

    if text == '':
        return text

    for c1, c2 in zip(text, text[1:]):

        if skip_next:
            skip_next = False
            continue

        if c1 == '-' or c1 == '_':
            output.append(c2.upper())
            skip_next = True
        else:
            output.append(c1)

    if not skip_next:
        output.append(text[-1])

    return ''.join(output)
