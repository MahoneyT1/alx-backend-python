#!/usr/bin/python3

"""Write a type-annotated function to_kv that takes a
string k and an int OR float
v as arguments and returns a tuple. The first element
of the tuple is the string k. The second element is the
square of the int/float v and should be annotated as a float.
"""
from typing import List, Union, Tuple



def to_kv(k: str, v: Union[int, float])-> Tuple[int, float]:
    new_tuple: tuple
    new_list: list = []
    
    new_list.append(k)
    new_list.append(v ** 2)

    new_tuple = tuple(new_list)
    return new_tuple
