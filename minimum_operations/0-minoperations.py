#!/usr/bin/python3

def minOperations(n):
    """
    Calculate the minimum number of operations to achieve n
    'H' characters in the file.

    Parameters:
    n (int): The target number of 'H' characters to achieve.

    Returns:
    int: The minimum number of operations required to achieve n characters.
    """
    
    # If n is less than or equal to 1, it's impossible to perform operations to achieve more characters
    if n <= 1:
        return 0

    # Initialize the operations count
    operations = 0

    # Iterate over all potential factors from 2 up to the square root of n
    for factor in range(2, int(n**0.5) + 1):
        # While n is divisible by this factor, divide n by the factor and increment the operations
        while n % factor == 0:
            operations += factor
            n //= factor

    # If n is still greater than 1 after the loop, it means it's a prime number
    # Add n itself to the operations count
    if n > 1:
        operations += n

    return operations
