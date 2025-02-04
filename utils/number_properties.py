from functools import lru_cache

from .armstrong import check_armstrong


@lru_cache(maxsize=None, typed=True)
async def check_properties(x: int) -> list[str, str]:
    """_summary_
    Args:
            x (int): _description_

    Returns:
            list[str, str]: _description_
    """
    properties = []
    armstrong = await check_armstrong(x)
    if armstrong:
        properties.append("armstrong")
    if x % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties
