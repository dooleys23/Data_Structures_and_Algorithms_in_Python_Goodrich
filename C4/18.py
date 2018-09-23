# C-4.18 Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.
import code
string = (raw_input('Please input a string:\n')).lower()
vowel = 0
constonant = 0
def str_iterate(indx):
    print string[indx]
    global vowel, constonant
    if indx == 0:
        print 'Completed'
        return None
    elif string[indx] in 'aeiou':
        vowel+=1
        str_iterate(indx-1)
    elif string[indx] in 'bcdfghjklmnpqrstvwxyz':
        print 'entered constonant'
        constonant+=1
        str_iterate(indx - 1)

print 'Vowels found [%i]' % vowel
print 'Constonant found [%i]' % constonant

str_iterate(len(string)-1)
code.interact(local=locals())