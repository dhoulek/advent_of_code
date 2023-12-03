import numpy as np
from numpy.linalg import norm

sensors = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace(':', '')
        line = line.replace(',', '')
        line = line.strip().split()
        sensors.append([np.array([int(line[i].split('=')[1]) for i in pos]) for pos in [[2, 3], [8, 9]]])
# print(sensors)

def check_line(l):
    pos = []
    for s, b in sensors:
        max_dist = norm(s-b, 1)
        if abs(l-s[1]) <= max_dist:
            delta = int(max_dist - abs(l-s[1]))
            # a = [norm(s-np.array([x, l]), 1) for x in range(s[0]-delta, s[0]+delta+1)]
            # print(max_dist, a)
            pos += [(x, l) for x in range(s[0]-delta, s[0]+delta+1)]
    return set(pos)

def remove_beacons(pos):
    beacons = set([tuple(b) for _, b in sensors])
    return pos-beacons

# print(remove_beacons(check_line(10)))
# print(sorted(check_line(10)))

print(f'there are {len(remove_beacons(check_line(2000000)))} impossible positions')