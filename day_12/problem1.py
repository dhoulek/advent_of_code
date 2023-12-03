from types import coroutine
import numpy as np

seg = []
with open('test.txt', 'r') as f:
    for line in f.readlines():
        x, y = line.strip().split('-')
        seg.append([x, y])
seg = np.array(seg)

caves = list(set(seg.reshape(seg.size)))
big = [c.isupper() for c in caves]
print(f'caves in the system: {caves}')
print(f'there are {sum(big)} BIG caves: {[caves[i] for i, c in enumerate(big) if c]}')

connections = np.zeros((len(caves), len(caves)), dtype=int)
for x, y in seg:
    connections[caves.index(x), caves.index(y)] = 1
    connections[caves.index(y), caves.index(x)] = 1
 
visits = np.zeros(len(caves), dtype=int)
visits[caves.index('start')] = 1
paths = []
 
def next_step(pos, visits):
    cont = []
    next = [c for c in range(len(caves)) if connections[pos, c]==1]
    for n in next:
        if n == caves.index('end'):
            cont.append([n])
        elif not big[n] and visits[n] == 1:
            cont.append([None])
        else:
            vis = visits.copy()
            vis[n] += 1            
            cont = cont + [[pos]+path for path in next_step(n, vis)]
    return cont

paths = next_step(caves.index('start'), visits)
num_valid_paths = 0
for p in paths:
    if p[-1] == caves.index('end'):
        num_valid_paths += 1
print(f'Number of possible paths: {num_valid_paths}')