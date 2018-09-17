'''
R.15
C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''
import code
list_raw_input = raw_input("Please input numbers seperated by a <,>:\n").split(",")
set_list = set(list_raw_input)

if len(list_raw_input) == len(set_list):
    print True
else:
    print False
