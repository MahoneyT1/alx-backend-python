#!/usr/bin/env python3
""" Typing and using Sequence ad list to perameterize"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function’s parameters and return
    values with the appropriate types
    """

    return [(i, len(i)) for i in lst]
