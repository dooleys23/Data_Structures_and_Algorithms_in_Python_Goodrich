# SD
# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.


str_raw_input = raw_input("Please input a string:\n")

lower_input = str_raw_input.lower()
counter = 0
for x in lower_input:
    if ord(x) == 97 or ord(x)== 101 or ord(x)== 105 or ord(x) == 111 or ord(x) == 117:
        counter +=1
print 'Vowels found in input: <%s>' % counter