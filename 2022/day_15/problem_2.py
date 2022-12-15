import numpy as np
import pandas as pd
from numpy.linalg import norm
from tqdm import tqdm

sensors = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace(':', '')
        line = line.replace(',', '')
        line = line.strip().split()
        sensors.append([np.array([int(line[i].split('=')[1]) for i in pos]) for pos in [[2, 3], [8, 9]]])
# print(sensors)

lim = (0, 4000000)
# lim = (0, 20)

def check_line(l):
    visible = []
    for s, b in sensors:
        max_dist = norm(s-b, 1)
        if abs(l-s[1]) <= max_dist:            
            delta = int(max_dist - abs(l-s[1]))
            visible.append([s[0]-delta, s[0]+delta])
    segments = pd.DataFrame(visible).sort_values(by=0)
    explored = lim[0]
    for lower, upper in zip(segments[0], segments[1]):
        if lower <= explored+1:
            explored = max(explored, upper)
        else:
            # print('***', explored, lower, upper)
            return [explored+1, l]
    return None

for l in tqdm(range(lim[0], lim[1]+1)):
    if check_line(l) != None:
        break
pos = check_line(l)
print(f'found on position: {pos}')
print(f'tuning frequency is: {pos[0]*4000000+pos[1]}')

# print(f'there are {check_line(2000000)} impossible positions')