# SD
# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).
std_input_list = []
print('Break the following with an EOF <CTRL> + <d>')

while True:
    try:
        std_input = raw_input('Please enter a string.')
        std_input_list.append(std_input)
    except EOFError:
        for x in reversed(std_input_list):
            print x
        break