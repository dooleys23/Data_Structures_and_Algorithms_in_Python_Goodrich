# C-4.15 Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).
# A subset is a set of elements whose elements can be found in another set, likely a large one

fruits = ['apple','banana','orange','grape']
fruits_subset = ['apple','banana','orange']

def check_for_subset(subset):
    print subset
    if subset == 0:
        print 'fruits_subset is a subset of fruits'
        'Completed'
    elif fruits_subset[subset] in fruits:
        print '%s was found in the set fruits' % fruits_subset[subset]

    check_for_subset(subset-1)


    #do work here

print check_for_subset(len(fruits_subset)-1)