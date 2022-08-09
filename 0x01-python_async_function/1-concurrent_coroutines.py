#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Import wait_random from the previous python file that
    youve written and write an async routine called wait_n
    that takes in 2 int arguments (in this order): n and max_delay.
    """

    return sorted([await wait_random(max_delay) for _ in range(n)])
