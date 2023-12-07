#!/usr/bin/env python3
"""100-safe_first_element"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of a list or None

    Args:
        lst (Sequence[Any]): list of elements

    Returns:
        Union[Any, None]: first element of list
    """
    if lst:
        return lst[0]
    else:
        return None
