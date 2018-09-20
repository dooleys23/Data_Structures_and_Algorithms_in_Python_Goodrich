x ='a'

try:
    print 'test'
    if x == 1:
        print 'This will never be printed'
    elif int(x) > 0:
        print 'Neither will this'
    else:
        print 'This should print...'
except:
    print 'This didnt work as expected'

print 'done'