from .armstrong import check_armstrong


async def check_properties(x: int) -> list[str, str]:
    """_summary_
    Args:
            x (int): _description_

    Returns:
            list[str, str]: _description_
    """
    properties = []
    if check_armstrong(x):
        properties.append("armstrong")
    if x % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties
