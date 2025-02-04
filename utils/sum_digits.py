cache = {}


def sum_digits(x: int) -> int:
    """
    Function to get the sum of the digits of a number.
    Args:
        x: int: Number whose digits are to be summed.
    """
    if x in cache:
        return cache[x]

    result = sum(int(digit) for digit in str(x))
    cache[x] = result
    return result
