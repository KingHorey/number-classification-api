import math
from async_lru import alru_cache


@alru_cache(maxsize=None, typed=True)
async def is_prime(x: int):
    """ Summary:
                Function to check if a given  number is a prime number

        Args:
                x (int): int to be checked

        Returns:
                bool: True if prime or False if not """

    if x < 2:
        return False
    if x == 3 or x == 2:
        return True

    if x % 2 == 0 or x % 3 == 0:
        return False

    i = 5
    x = abs(x)

    while i <= math.sqrt(x):
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6

    return True
