# P1.29
# Write a Python program that outputs all possible strings formed by using
# the characters c,a,t,d,o and g exactly once.
import code
vowel_str = 'catdo'

str1, str2, str3, str4, str5 = [], [], [], [], []
for a in vowel_str:
    str1.append(a)
    for b in vowel_str:
        b_str = a,b
        str2.append(','.join(str(i) for i in b_str))
        for c in vowel_str:
            c_str = a,b,c
            str3.append(','.join(str(i) for i in c_str))
            for d in vowel_str:
                d_str = a,b,c,d
                str4.append(','.join(str(i) for i in d_str))
                for e in vowel_str:
                    e_str = a,b,c,d,e
                    str5.append(','.join(str(i) for i in e_str))

print[i for i in str1]
print[i for i in str2]
print[i for i in str3]
print[i for i in str4]
print[i for i in str5]