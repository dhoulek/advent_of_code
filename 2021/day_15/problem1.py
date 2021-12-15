import numpy as np

input = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input.append([int(c) for c in line.strip()])
input = np.array(input)

print(f'dimensions of input: {input.shape}')

dim = input.shape[0]
risks = np.zeros(input.shape, dtype=int)
for i in np.arange(1, dim):
    risks[i, 0] = risks[i-1, 0] + input[i, 0]
    for j in np.arange(1, i):
        risks[j, i-j] = input[j, i-j] + min(risks[j-1, i-j], risks[j, i-j-1])
    risks[0, i] = risks[0, i-1] + input[0, i]

for i in np.arange(1, dim):
    for j in np.arange(i, dim):
        risks[j, dim+i-1-j] = input[j, dim+i-1-j] + min(risks[j-1, dim+i-1-j], 
                                                        risks[j, dim+i-1-j-1])       
print(risks)
print(f'risk score: {risks[-1, -1]}')