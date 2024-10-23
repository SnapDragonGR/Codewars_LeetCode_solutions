"""
Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
"""

# Solution:

def tower_builder(n_floors):
    tower = []
    for i in range(1, n_floors + 1):
        spaces = n_floors - i
        stars = 2 * i - 1

        floor = ' ' * spaces + '*' * stars + ' ' * spaces

        tower.append(floor)

    return tower