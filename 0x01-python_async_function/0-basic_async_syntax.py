#!/usr/bin/env python3
'''
Asynchronnos python programming 
'''
import asyncio
import random


async def wait_random(max_delay: int = 10)-> float:
    '''
    an asyncronious co-routine
    '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return (wait)
