'''
SD
R-1.13
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
'''
max_count = int(raw_input('Please enter a number...:'))
odd_list = []
for x in range(max_count):
    for y in range(max_count):
        if (x*y) % 2 != 0:
            odd_list.append((x,y))

for x in odd_list:
    print x