'''
SD
R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.

Ex: using bitwise operators, similar to subnetting, we can check bit 0, which is 2^0 == 1.
'''


def is_even(k):
    if k & 0:
        return True
    else:
        return False

print is_even(int(raw_input('Please enter a number:\n')))