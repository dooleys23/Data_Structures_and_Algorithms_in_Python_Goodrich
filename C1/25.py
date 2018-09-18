# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example,
# if given the string "Let s try, Mike.", this function would return
# "Lets try Mike"

inp = raw_input('Please input a sentence, which has comma structure:\n--->')
inp_no_comma = inp.replace(',','')

print inp_no_comma