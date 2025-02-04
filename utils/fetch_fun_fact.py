import httpx


def get_fun_fact(x: int):
    """_summary_

        Args:
                        x (int): _description_

        Returns:
                        str: _description_
        """
    url = f"http://numbersapi.com/{x}/math"
    response = httpx.get(url)
    return response.text
