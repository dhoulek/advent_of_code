import re

file = open('2.in', 'r')
valid = 0
valid2 = 0
for line in file.readlines():
    limits, char, pw = line.rstrip().split(' ')
    lower, upper = [int(x) for x in limits.split('-')]
    char = char[0]
    count = sum([1 if ch==char else 0 for ch in pw])
    if lower<=count and count<=upper:
        valid +=1
    if (pw[lower-1]==char) + (pw[upper-1]==char) == 1:
        valid2 += 1
print(valid)
print(valid2)