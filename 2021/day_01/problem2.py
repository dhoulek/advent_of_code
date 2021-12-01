import numpy as np

with open('input.txt', 'r') as f:
    data = np.loadtxt(f, dtype=np.int)
print(len(data))

count = lambda l: np.sum([1 if e<0 else 0 for e in l])

dat = data[:-2] + data[1:-1] + data[2:]
print('number of increases: ', count(dat[:-1]-dat[1:]))