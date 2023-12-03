import numpy as np

def abundancy(code):
    num_lines = len(code)
    line_length = len(code[0])
    sums = [sum([code[i][j] for i in range(num_lines)]) for j in range(line_length)]
    return sums

input = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input.append([int(x) for x in list(line.strip())])        
print(f'input has {len(input)} lines, each {len(input[0])} bits long')

code = input.copy()
bit = 0
while(len(code)>1):
    sums = abundancy(code)
    if (sums[bit] >= len(code)/2):
        keep = 1
    else:
        keep = 0
    new = [line for line in code if line[bit]==keep]
    code = new
    bit += 1
    
O2_str = ''.join([str(s) for s in code[0]])
O2 = int(O2_str, 2)
print(f'O2 = {O2_str} = {O2}')
    
code = input.copy()
bit = 0
while(len(code)>1):
    sums = abundancy(code)
    if (sums[bit] >= len(code)/2):
        keep = 0
    else:
        keep = 1
    new = [line for line in code if line[bit]==keep]
    code = new
    bit += 1
    
CO2_str = ''.join([str(s) for s in code[0]])
CO2 = int(CO2_str, 2)
print(f'CO2 = {CO2_str} = {CO2}')

print(f'O2 * CO2 = {O2*CO2}')