import httpx

fun_fact_cache = {}


def get_fun_fact(x: int) -> str:
    """
    Function to get a fun fact about a number.
    Args:
        x: int: Number for which to get the fun fact.
    Returns:
        str: Fun fact about the number.
    """
    if x in fun_fact_cache:
        return fun_fact_cache[x]

    url = f"http://numbersapi.com/{x}/math"
    response = httpx.get(url)
    fun_fact_cache[x] = response.text
    return response.text
