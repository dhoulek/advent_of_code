import numpy as np
from numpy.core.numeric import full_like

input = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input.append([int(c) for c in line.strip()])
input = np.array(input)
print(f'dimensions of input: {input.shape}')

full = np.zeros([d*5 for d in input.shape], dtype=int)
for j in range(input.shape[0]):
    for i in range(input.shape[1]):
        for y in range(5):
            for x in range(5):
                full[y*input.shape[0]+j, x*input.shape[1]+i] = (input[j, i]+x+y-1)%9 + 1
print(f'dimensions of the full map: {full.shape}')

def update_diag_upper(risks, i):
    update = False
    new = risks.copy()
    m = min(risks[i, 0],
            risks[i-1, 1] + input[i, 1] + input[i, 0])
    if m < risks[i, 0]:
        update = True
        new[i, 0] = m
        print('*')
    for j in range(1, i):
        m = min(risks[j, i-j],
                risks[j+1, i-j-1] + input[j+1, i-j] + input[j, i-j],
                risks[j-1, i-j+1] + input[j, i-j+1] + input[j, i-j])
        if m < risks[j, i-j]:
            update = True
            new[j, i-j] = m
            print('**')
            # print(m, risks[j, i-j])
    m = min(risks[0, i],
            risks[1, i-1] + input[1, i] + input[0, i])
    if m < risks[0, i]:
            update = True
            new[0, i] = m
            print('***')
    return update, new

def update_diag_lower(risks, i):
    update = False
    new = risks.copy()
    m = min(risks[i, dim-1],
            risks[i+1, dim-2] + input[i+1, dim-1] + input[i, dim-1])
    if m < risks[i, dim-1]:
        update = True
        new[i, dim-1] = m
        print('*')
    for j in range(i, dim):
        m = min(risks[j, dim+i-1-j],
                risks[j+1, dim+i-1-j-1] + input[j+1, dim+i-1-j] + input[j, dim+i-1-j],
                risks[j-1, dim+i-1-j+1] + input[j, dim+i-1-j+1] + input[j, dim+i-1-j])
        if m < risks[j, dim+i-1-j]:
            update = True
            new[j, dim+i-1-j] = m
            print('**')
            # print(m, risks[j, dim+i-1-j])
    m = min(risks[dim-1, i],
            risks[dim-2, i+1] + input[dim-1, i+1] + input[dim-1, i])
    if m < risks[0, i]:
            update = True
            new[0, i] = m
            print('***')
    return update, new

input = full
dim = input.shape[0]
risks = np.zeros(input.shape, dtype=int)
for i in np.arange(1, dim):
    risks[i, 0] = risks[i-1, 0] + input[i, 0]
    for j in np.arange(1, i):
        risks[j, i-j] = input[j, i-j] + min(risks[j-1, i-j], risks[j, i-j-1])
    risks[0, i] = risks[0, i-1] + input[0, i]
    update = True
    print(f'i={i}')
    # print(input)
    # print(risks)
    while update:
        update, risks = update_diag_upper(risks, i)
        if update:
            print(f'diagonal updated for i={i}')    
    # print('new:')
    # print(risks)

for i in np.arange(1, dim):
    for j in np.arange(i, dim):
        risks[j, dim+i-1-j] = input[j, dim+i-1-j] + min(risks[j-1, dim+i-1-j], 
                                                        risks[j, dim+i-1-j-1])       
    update = True
    print(f'i={i}')
    # print(input)
    # print(risks)
    while update:
        update, risks = update_diag_upper(risks, i)
        if update:
            print(f'diagonal updated for i={i}')    
    # print('new:')
    # print(risks)
print(risks)
print(f'risk score: {risks[-1, -1]}')