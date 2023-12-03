#test
xmin=20
xmax=30
ymin=-10
ymax=-5

# #input
xmin=137
xmax=171
ymin=-98
ymax=-73


from itertools import product
import numpy as np
from tqdm import tqdm

ini = []

def check_target(x, y):
    return xmin<=x and x<=xmax and ymin<=y and y<=ymax

for v0x, v0y in tqdm(product(np.arange(0, 200), np.arange(-100, 200))):
    x = 0
    y = 0
    vx = v0x
    vy = v0y
    while (vx>0  or (vx==0 and xmin<=x and x<=xmax)) and y>ymin:
            x += vx
            y += vy
            if xmin<=x and x<=xmax and ymin<=y and y<=ymax:
                ini.append((v0x, v0y))            
                break
            else:
                vx = max(0, vx-1)
                vy -= 1



print('initial velocities:')
print(ini)
print()
print(f'found {len(ini)} initial velocities hitting the target')