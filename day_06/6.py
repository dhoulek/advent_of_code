def count_answers2(s):    
    return sum([sum([ch in s1 for s1 in s.split()])==len(s.split()) for ch in 'abcdefghijklmnopqrstuvwxyz'])
 
def count_answers(s):
    return sum([ch in s for ch in 'abcdefghijklmnopqrstuvwxyz'])

input = open('6.in', 'r')

yes = 0
answers = ''

for line in input.readlines():
    line = line.rstrip()
    if line == '':
        yes += count_answers2(answers)
        answers = ''
    else:
        answers += ' '+line
if answers != '':
    yes += count_answers2(answers)
input.close()

print(yes)