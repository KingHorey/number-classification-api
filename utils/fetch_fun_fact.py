
from async_lru import alru_cache
import httpx


@alru_cache(maxsize=None, typed=True)
async def get_fun_fact(x: int) -> str:
    """
    Function to get a fun fact about a number.
    Args:
        x: int: Number for which to get the fun fact.
    Returns:
        str: Fun fact about the number.
    """
    async with httpx.AsyncClient() as client:
        url = f"http://numbersapi.com/{x}/math"
        response = await client.get(url)
        return response.text
