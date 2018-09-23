# C-4.16 Write a short recursive Python function that takes a character string s and
# outputs its reverse. For example, the reverse of pots&pans would be
# snap&stop .

raw_str = raw_input('Please input a string...')
backwards_str = ''

def read_backwards(indx):
    global backwards_str
    if indx == 0:
        print raw_str[indx], indx
        backwards_str += (raw_str[indx])
        return 'completed'

#    raw_str.append(raw_str[indx])
#    backwards_str += raw_str[indx]
    elif indx >= 0:
        print raw_str[indx], indx
        backwards_str += (raw_str[indx])
    read_backwards(indx-1)
read_backwards(len(raw_str)-1)

print backwards_str

# Output Please input a string...pots and pans
# s 12
# n 11
# a 10
# p 9
#   8
# d 7
# n 6
# a 5
#   4
# s 3
# t 2
# o 1
# p 0
# snap dna stop