import numpy as np
from tqdm import tqdm
from itertools import product

# Read input from file
with open('input.txt', 'r') as f:
    board = np.array([np.array(list(l.strip())) for l in f.readlines()])

n, m = board.shape
stones = []
x_fixes = {x: [] for x in range(m)}
y_fixes = {y: [] for y in range(n)}

# Extract information about stones and fixations in the initial state
for y, x in product(range(n), range(m)):
    if board[y, x] == 'O':
        stones.append([y, x])
    elif board[y, x] == '#':
        x_fixes[x].append(y)
        y_fixes[y].append(x)

ini_stones = stones.copy()

# Sorting functions for sorting stones based on x and y coordinates
x_sort = lambda p: p[1]
y_sort = lambda p: p[0]

# Functions to tilt stones in different directions
def tilt_north(stones):    
    # Helper function to update free positions after tilting north
    def update_free(y):    
        for x in y_fixes[y]:
            last_free[x] = y + 1
    stones = sorted(stones, key=y_sort)
    last_free = [0] * m
    y = 0
    update_free(y)
    for i, s in enumerate(stones):
        for yy in range(y, s[0]):
            update_free(yy)
        y = s[0]
        stones[i][0] = last_free[s[1]]
        last_free[s[1]] += 1
    return stones

def tilt_south(stones):    
    # Helper function to update free positions after tilting south
    def update_free(y):
        for x in y_fixes[y]:
            last_free[x] = y - 1    
    stones = sorted(stones, key=y_sort, reverse=True)
    last_free = [n - 1] * m
    y = n - 1
    update_free(y)
    for i, s in enumerate(stones):
        for yy in range(y, s[0], -1):
            update_free(yy)
        y = s[0]
        stones[i][0] = last_free[s[1]]
        last_free[s[1]] -= 1
    return stones

def tilt_east(stones):    
    # Helper function to update free positions after tilting east
    def update_free(x):
        for y in x_fixes[x]:
            last_free[y] = x - 1    
    stones = sorted(stones, key=x_sort, reverse=True)
    last_free = [m - 1] * n
    x = m - 1
    update_free(x)
    for i, s in enumerate(stones):
        for xx in range(x, s[1], -1):
            update_free(xx)
        x = s[1]
        stones[i][1] = last_free[s[0]]
        last_free[s[0]] -= 1
    return stones

def tilt_west(stones):    
    # Helper function to update free positions after tilting west
    def update_free(x):
        for y in x_fixes[x]:
            last_free[y] = x + 1    
    stones = sorted(stones, key=x_sort)
    last_free = [0] * n
    x = 0
    update_free(x)
    for i, s in enumerate(stones):
        for xx in range(x, s[1]):
            update_free(xx)
        x = s[1]
        stones[i][1] = last_free[s[0]]
        last_free[s[0]] += 1
    return stones

# Function to perform a cycle of tilting in all directions
def cycle(stones):
    return tilt_east(tilt_south(tilt_west(tilt_north(stones))))

# Function to get a hash representation of the stone positions
def get_hash(stones):
    stones = sorted(sorted(stones, key=x_sort), key=y_sort)
    return ''.join([f'{s[0]},{s[1]};' for s in stones])

# Initial tilt north to set up the starting configuration
stones = tilt_north(stones)
load = sum([n - s[0] for s in stones])

# Print Part 1 result
print('Part 1:')
print(f'The total load on the north support beams is {load}\n')

# Part 2
stones = ini_stones.copy()
cycles = []

# Iterate through cycles and detect repetitions
for i in range(1000):
    stones = cycle(stones)
    hash = get_hash(stones)
    if hash in cycles:
        period = i - cycles.index(hash)
        offset = len(cycles) - period
        print(f'Found repetition {i}: period={period} offset={offset}')
        break
    cycles.append(hash)

# Calculate the result for Part 2 based on the repetition information
N_cycles = 1000000000
i = (N_cycles - offset) % period
hash = cycles[i + offset - 1]
stones = hash[:-1].split(';')
stones = [[int(s.split(',')[0]), int(s.split(',')[1])] for s in stones]
load = sum([n - s[0] for s in stones])

# Print Part 2 result
print(f'The total load on the north support beams is {load}')