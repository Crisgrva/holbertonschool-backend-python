#!/usr/bin/env python3
"""1. Async Comprehensions"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Import async_generator from the previous task
    and then write a coroutine called
    async_comprehension that takes no arguments.
    """
    return [num async for num in async_generator()]