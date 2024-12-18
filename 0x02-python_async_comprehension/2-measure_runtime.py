#!/usr/bin/env python3
"""Import async_comprehension from the previous
file and write a measure_runtime coroutine that will
execute async_comprehension four times in parallel using
asyncio.gather. measure_runtime should measure the total
runtime and return it. Notice that the total runtime is
roughly 10 seconds, explain it to yourself.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measuring time with measure runtime function it
    check the total amount of time taken to run the function
    """
    start = time.time()
    async_exec = [async_comprehension() for _ in range(4)]
    result = await asyncio.gather(*async_exec)
    end = time.time()
    total_runtime = end - start

    return total_runtime
