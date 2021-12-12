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

def check_small(visits):
    num_small_twice = 0
    too_many = False
    for c in range(len(caves)):
        if not big[c] and visits[c]>1:
            if visits[c]>2:
                too_many = True
            num_small_twice += 1
    return num_small_twice<2 and not too_many
 
def next_step(pos, visits):
    cont = []
    next = [c for c in range(len(caves)) if connections[pos, c]==1]
    for n in next:
        if not big[n] and not check_small(visits):
            cont.append([None])
        elif n == caves.index('end'):
            cont.append([n])
        elif n == caves.index('start'):
            cont.append([None])
        else:
            vis = visits.copy()
            vis[n] += 1            
            cont = cont + [[n]+path for path in next_step(n, vis) if path[-1] != None]
    return cont

paths = next_step(caves.index('start'), visits)
num_valid_paths = 0
for p in paths:
    # p = [caves.index('start')]+p
    if p[-1] == caves.index('end'):
        # print(','.join([caves[c] for c in p]))
        num_valid_paths += 1
print(f'Number of possible paths: {num_valid_paths}')