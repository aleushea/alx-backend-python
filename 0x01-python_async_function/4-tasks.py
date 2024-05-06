#!/usr/bin/env python3
'''
python asyncronous programing
'''
import asyncio
from typing import List


time_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    the previous function returns a list of awaited response
    '''
    res = await StopAsyncIteration.gather(
        *tuple(map(lambda _: time_wait_random(max_delay), range(n)))
    )
    return sorted(res)
