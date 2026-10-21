# Week 4, Session 2: Task 2

# Given an incomplete function divide_and_remainder with a docstring.
# Your task is to complete the function based on the details in the 
# docstring.

def divide_and_remainder(dividend, divisor):
    """
    This function performs integer division and returns both the quotient
    and the remainder.

    Args:
        dividend (int): The number to be divided.
        divisor (int): The number by which the dividend is divided.

    Returns:
        tuple: A tuple containing (quotient, remainder).
    """

    # complete your code here

    # Returning both quotient and remainder
    return quotient, remainder

# Check if correct output is produced
quotient, remainder = divide_and_remainder(10, 3)
print(f"Quotient: {quotient}")    # Output: Quotient: 3
print(f"Remainder: {remainder}")  # Output: Remainder: 1

# Directly print the returned tuple
print(divide_and_remainder(33, 3))  # Output: (11, 0)
