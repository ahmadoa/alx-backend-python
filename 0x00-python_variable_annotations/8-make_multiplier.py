#!/usr/bin/env python3
"""8-make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns result of multiplying a float by multiplier

    Args:
        multiplier (float): float number to multiply

    Returns:
        Callable: function that multiplies a float by a multiplier
    """
    return lambda x: x * multiplier
