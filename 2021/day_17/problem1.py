#test
xmin=20
xmax=30
ymin=-10
ymax=-5

#input
xmin=137
xmax=171
ymin=-98
ymax=-73


from itertools import product
import numpy as np
from tqdm import tqdm

hmax = 0

def check_target(x, y):
    return xmin<=x and x<=xmax and ymin<=y and y<=ymax

for v0x, v0y in tqdm(product(np.arange(0, 50), np.arange(-100, 400))):
    x = 0
    y = 0
    vx = v0x
    vy = v0y
    h = 0
    while not check_target(x,y) and \
        ((vx>0 and y>ymax) or \
        (vx==0 and xmin<=x and x<=xmax and y>ymax)):
            x += vx
            y += vy
            h = max(h, y)
            vx = max(0, vx-1)
            vy -= 1               
    if check_target(x, y):
        if h>hmax:
            hmax = h
            best_shot = (v0x, v0y)
            # print(f'found new maximum height of {h} for {best_shot}')

print(f'found maximum height of {hmax} for {best_shot}')