# C-4.9 Write a short recursive Python function that finds the minimum and maximum
# values in a sequence without using any loops.

import code
set = ['1','22','6549','1000','304','21']

class result():
    def __init__(self,max,min):
        self._max = max
        self._min = min

x= result(None,None)

def find_max_min(number):
    # print'step'
    print number
    if number == 0:
        print 'Completed'
    else:
        if number > x._max:
            x._max = number
            print "New Max Number is %s " % number
            find_max_min(number - 1)
        elif number < x._max:
            min_num = number
            print "New Min Number is %s " % number
            find_max_min(number - 1)
        else:
            find_max_min(number - 1)


find_max_min(len(set))
code.interact(local=locals())