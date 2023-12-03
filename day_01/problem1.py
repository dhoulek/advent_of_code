import numpy as np

with open('input.txt', 'r') as f:
    data = np.loadtxt(f, dtype=np.int)
print(len(data))

count = lambda l: np.sum([1 if e<0 else 0 for e in l])

print('number of increases: ', count(data[:-1]-data[1:]))