from async_lru import alru_cache


@alru_cache(maxsize=None, typed=True)
async def sum_digits(x: int) -> int:
    """
    Function to get the sum of the digits of a number.
    Args:
        x: int: Number whose digits are to be summed.
    """
    x = abs(x)
    result = sum(int(digit) for digit in str(x))
    return result
