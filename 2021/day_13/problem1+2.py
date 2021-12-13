import numpy as np
from tqdm import tqdm

points = []
folds = []
instuctions = False
maxx = 0
maxy = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        if line.strip() == '':
            instuctions = True
        else:
            if not instuctions:
                x, y = line.strip().split(',')
                x = int(x)
                y = int(y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
                points.append([int(x), int(y)])
            else:
                ax, x = line.strip().split(' ')[-1].split('=')
                folds.append([ax, int(x)])

def print_data(data):
    for y in range(data.shape[0]):
        line = ''
        for x in range(data.shape[1]):
            if data[y, x] == 0:
                line += '.'
            else:
                line += '#'                
        print(line)
           
def fold(data, ax, pos):
    if ax == 'x':
        if data.shape[1]>2*pos+1:
            print('we need more zeros on top')
        new = data[:, :pos]
        for i in np.arange(pos+1, data.shape[1]):
            for j in np.arange(data.shape[0]):
                new[j, data.shape[1]-1-i] = new[j, data.shape[1]-1-i] or data[j, i]
    if ax == 'y':
        if data.shape[0]>2*pos+1:
            print('we need more zeros on left')
        new = data[:pos, :]
        for j in np.arange(pos+1, data.shape[0]):
            for i in np.arange(data.shape[1]):
                new[data.shape[0]-1-j, i] = new[data.shape[0]-1-j, i] or data[j, i]
    return new

data = np.zeros((maxy+1, maxx+1), dtype=int)

for x, y in points:
    data[y, x] = 1
# print_data(data)

for ax, pos in folds[:1]:
    data = fold(data, ax, pos)
# print_data(data)    
print(f'number of points after 1 fold: {sum(data.reshape((data.size, 1)))[0]}')

for ax, pos in tqdm(folds[1:]):
    data = fold(data, ax, pos)
print_data(data)


