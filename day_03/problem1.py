import numpy as np

input = ''
num_lines = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input += line.strip()
        num_lines += 1
line_length = int(len(input)/num_lines)
print(f'input has {num_lines} lines, each {line_length} bits long')

sums = np.zeros(line_length)
for i, c  in enumerate(input):
    if int(c) == 1:
        sums[i%line_length] += 1
gamma = ''
epsilon = ''
for val in sums:
    if val > num_lines/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
        
g = int(gamma, 2)        
e = int(epsilon, 2)
print(f'gamma = {gamma} = {g}')
print(f'epsilon = {epsilon} = {e}')
print(f'solutiom = {g*e}')