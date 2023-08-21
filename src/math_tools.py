""" Simple math test case for unit testing.

Functions:
    double: Multiplies a value by 2
    triple: Multiplies a value by 3
    square: Multiplies a value by the number of times

"""


def triple(n: int) -> int:
    """ Return a value of itself multiplied by 3."""
    if not isinstance(n, int):
        raise TypeError
    return n * 3


def square(n) -> int:
    """ Return a value times itself twice."""
    if not isinstance(n, (int, float)):
        raise TypeError
    return n * n


""" Version 1

def triple(x):
    total = 0
    for i in range(3):
        total += x
    return total

def square(x):
    if x < 0:
        x = x * -1
    total = 0
    for i in range(x):
        total += x
    return total
"""
