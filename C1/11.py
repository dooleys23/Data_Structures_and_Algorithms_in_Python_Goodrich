'''
SD
R-1.11
Demonstrate list comprehension to produce the all possible values of 8 bits
'''
#
x = 256
a_list = [(1<<x) for x in range(9)]
print a_list