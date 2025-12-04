"""
math_operations.py

A module containing basic mathematical operations.
"""


def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """
    Returns the quotient of a divided by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base, exponent):
    """Returns base raised to the power of exponent."""
    return base ** exponent


def sqrt(n):
    """
    Returns the square root of n.
    Raises ValueError if n is negative.
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return n ** 0.5


def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
