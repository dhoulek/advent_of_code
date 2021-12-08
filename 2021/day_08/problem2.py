import numpy as np

def sort(l):
    return [''.join(sorted(list(i))) for i in l]

final_sum = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        lengths = {i: [] for i in np.arange(2,8)}
        input = sort(line.split('|')[0].split())
        code = sort(line.split('|')[-1].split())
        for digit in input:
            lengths[len(digit)].append(set(digit))
        
        digits = ['']*10
        digits[1] = set(lengths[2][0])
        digits[4] = set(lengths[4][0])
        digits[7] = set(lengths[3][0])
        digits[8] = set(lengths[7][0])
        for s in lengths[5]:
            if digits[1].issubset(s):
                digits[3] = s
        for s in lengths[5]:
            if set(digits[4]-digits[1]).issubset(set(s)):
                digits[5] = s
        for s in lengths[5]:
            if s != digits[3] and s != digits[5]:
                digits[2] = s
        for s in lengths[6]:
            if not digits[1].issubset(s):
                digits[6] = s
        for s in lengths[6]:
            if digits[4].issubset(s):
                digits[9] = s
        for s in lengths[6]:
            if s != digits[6] and s != digits[9]:
                digits[0] = s
        
        decode = {''.join(sorted(list(c))): i for i, c in enumerate(digits)}
        
        result = int(''.join([str(decode[c]) for c in code]))
        print(result)
        final_sum += result
        
print(f'Total sum: {final_sum}')
            
            