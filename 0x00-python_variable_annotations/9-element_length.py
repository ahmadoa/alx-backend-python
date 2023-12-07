#!/usr/bin/env python3
"""9-element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples with first value as a string & the second

    Args:
        lst (List[Tuple]): list of tuples

    Returns:
        List[Tuple[str, int]]: list of tuples with the first value as a string
    """
    return [(i, len(i)) for i in lst]
