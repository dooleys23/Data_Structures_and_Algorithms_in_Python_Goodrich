'''
SD
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''
import math, code

def sqrt_total(i):
    total_sqrt_sum = float(0)
    for x in range(i):
        if x % 2 != 0:
#            code.interact(local=locals())
            total_sqrt_sum += math.sqrt(x)
    return total_sqrt_sum

print sqrt_total(int(raw_input('Chose a number?:\n')))
