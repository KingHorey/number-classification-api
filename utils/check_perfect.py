from async_lru import alru_cache
import math


@alru_cache(maxsize=None, typed=True)
async def is_perfect(x: int) -> bool:
    """_summary_

    Args:
            x (int): _description_

    Returns:
            bool: _description_

    """
    x = abs(x)
    if x < 2:
        return False
    divisor = [1]
    round_num = int(math.sqrt(x) + 1)
    i = 2
    for i in range(2, round_num):
        if x % i == 0:
            divisor.append(i)
            if i != x // i:
                divisor.append(x // i)
    return sum(divisor) == x
