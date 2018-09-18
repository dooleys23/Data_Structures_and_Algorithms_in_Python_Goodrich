'''
SD
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''
import random

def minmax(rand_list_len):
    rand_list = []
    smallest_possible, largest_possible = int(raw_input('smallest possible int?:\n')), int(raw_input('largest possible int?:\n'))
    switch = True
    smallest_int = None
    largest_int = None
    for x in range(rand_list_len):
        if switch == True:
            generated_int = random.randint(smallest_possible,largest_possible)
            rand_list.append(generated_int)
            smallest_int = int(generated_int)
            largest_int  = int(generated_int)
            switch = False
        else:
            generated_int = random.randint(smallest_possible, largest_possible)
            rand_list.append(generated_int)
            if generated_int > largest_int:
                largest_int = generated_int
            elif generated_int < smallest_int:
                smallest_int = generated_int
    return(smallest_int,largest_int)

print minmax(int(raw_input('How many numbers would you like generated?:\n')))

