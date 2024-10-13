#!/usr/bin/env python3

"""Write a type-annotated function sum_mixed_list which
takes a list mxd_lst of integers and floats and returns
their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats and returns
    their sum as a float.
    """
    counter = 0

    for i in range(len(mxd_lst)):
        counter += mxd_lst[i]
    return counter
