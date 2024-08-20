"""
Some but not all
Description
Your task is to create a function that given a sequence and a predicate,
returns True if only some (but not all) the elements in the sequence are True
after applying the predicate

Examples
('abcdefg&%$', x -> isLetter(x)) == true
('&%$=', x -> isLetter x) == false
('abcdefg', x -> isLetter x) == false

([4, 1], x -> x > 3) == true
([1, 1], x -> x > 3) == false
([4, 4], x -> x > 3) == false
"""

# Solution:


def some_but_not_all(seq, pred):
    true_count = 0
    false_count = 0

    for element in seq:
        if pred(element):
            true_count += 1
        else:
            false_count += 1

    if true_count > 0 and false_count > 0:
        return True
    else:
        return False