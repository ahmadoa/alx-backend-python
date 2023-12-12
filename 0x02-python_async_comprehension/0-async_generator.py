#!/usr/bin/env python3
"""0-async_generator module"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """wait 1 sec then yield a random number 1-10"""
    arr = []
    for _ in range(10):
        arr.append(random.uniform(0, 10))
    for i in arr:
        await asyncio.sleep(1)
        yield i
