'''
SD
C18 Demonstrate how to use python's list comprehension syntax to produce
[0,2,6,12,20,30,42,56,72,90]


count = 0
iteration_list = []
for x in range(0,20,2):
    count = count + x
    iteration_list.append(count)

print(iteration_list)
'''
# lists comprehensions can only contain expressions. count = count + 1 is an assignment (statement)
# so you cannot use it there

print[int((x*x)+x) for x in range(10)]
