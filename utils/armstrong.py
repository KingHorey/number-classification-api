import math
from async_lru import alru_cache


@alru_cache(maxsize=None, typed=True)
async def check_armstrong(x: int):
    """_summary_

    Args:
            x (int): _description_
    """
    x = abs(x)
    number_in_string = str(x)
    number_length = len(number_in_string)  # get the length of the number
    output = 0
    for i in number_in_string:
        output += math.pow(int(i), int(number_length))
    return output == x
