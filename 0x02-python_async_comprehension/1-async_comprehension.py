#!/usr/bin/env python3
''' Asynchronous Python '''
import random
import asyncio
from typing import Generator
async_comprehension = __import__('0-async_generator').async_generator


async def async_comprehension2() -> Generator[float, None, None]:
    '''yield a random number at 1sec interval'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
