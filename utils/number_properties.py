from async_lru import alru_cache

from .armstrong import check_armstrong


@alru_cache(maxsize=None, typed=True)
async def check_properties(x: int) -> list[str]:
    """_summary_
    Args:
            x (int): _description_

    Returns:
            list[str]: _description_
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
