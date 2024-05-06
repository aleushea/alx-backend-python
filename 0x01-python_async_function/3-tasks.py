#!/usr/bin/env python3
'''
python asynchronous programming 
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    int is an input asyncio task is the return
    '''
    return asyncio.create_task(wait_random(max_delay))
