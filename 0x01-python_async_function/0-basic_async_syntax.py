#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named
wait_random that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.

Use the random module.
"""
import asyncio
import random


wait_random: float


async def wait_random(max_delay: int=10):
    """Function that returns a float delay number"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


if __name__ == "__main__":
    asyncio.run(wait_random())
