# SD
# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b.


a,b = [],[]
n = int(raw_input('Please enter a length for n: ')) + 1
c=[]
for x in range(n):
    a.append(x)
    b.append(x)
    c.append(a[x]*b[x])

print c