#!/usr/bin/env python3

"""Write a type-annotated function floor which takes a float
n as argument and returns the floor of the float.
"""

import math


def floor(n: float) -> int:
    """Using math.floor to round the n down to minimum
    """
    result = math.floor(n)
    return result
