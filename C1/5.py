'''
SD
R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
'''
import math
total = sum([math.sqrt(i) for i in range(int(raw_input('Please input the max int:\n'))) if i % 2 == 0])
print total