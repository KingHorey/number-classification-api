def sum_digits(x: int) -> int:
    """
            Function to get the sum of the digits of a number.
            Args:
                    x: int: Number whose digits are to be summed.
    """
    # Initialize sum to 0
    sum = 0
    print('in int', x)

    # Iterate over the digits of the number
    while x != 0:
        # Add the last digit to the sum
        sum += x % 10

        # Remove the last digit
        x = x // 10

    # Return the sum of the digits
    return sum
