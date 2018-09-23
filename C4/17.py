# C-4.17 Write a short recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.

raw_str = raw_input("Please input a string to check if it's a palindrome...")
backwards_str = ''

def read_backwards(indx):
    global backwards_str
    if indx == 0:
        backwards_str += (raw_str[indx])
        return 'Completed'
#    raw_str.append(raw_str[indx])
#    backwards_str += raw_str[indx]
    elif indx >= 0:
        print raw_str[indx], indx
        backwards_str += (raw_str[indx])
    read_backwards(indx-1)
read_backwards(len(raw_str)-1)

if raw_str == backwards_str:
    print 'string is a palindrome'
else:
    print 'string is not a palindrome'