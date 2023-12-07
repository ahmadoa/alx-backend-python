#!/usr/bin/env python3
"""101-safely_get_value"""
from typing import Any, Mapping, Union, TypeVar

T = TypeWar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default = Union[T, None] = None) -> Union[Any, T]:
    """safely_get_value function

    Args:
        dct (Mapping): dictionary
        key (Any): key
        default (Union[TypeVar('T'), None], optional):
            default value
    
    Returns:
        Union[Any, TypeVar['T']]: value
    """
    if key in dct:
        return dct[key]
    else:
        return default
