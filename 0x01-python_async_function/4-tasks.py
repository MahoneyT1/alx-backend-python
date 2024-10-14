#!/usr/bin/env python3

"""Take the code from wait_n and alter it into a new
function task_wait_n. The code is nearly identical to
wait_n except task_wait_random is being called.
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n should return the list of all the delays
    (float values). The list of the delays should be in
    ascending order without using sort() because of
    concurrency.
    """

    result = []

    for _ in range(n):
        result.append(await wait_random(max_delay))

    result = sorted(result)
    return result
