# SD
# C-1.19 Demonstrate how to use Pythons list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

print ','.join([chr(int(x)) for x in range(97, 122)])
