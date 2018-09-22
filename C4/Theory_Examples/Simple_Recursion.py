# Example found in https://www.youtube.com/watch?v=eqQQoIAT9So

def countdown(number):
    if set[number] == 0:
        print ('Completed')
    else:
        print number
        countdown(number-1)

set = {2,3,4,5,6,7}

countdown(len(set))