# keep depth of empty positions below `height` for each shape and 
# detect when it starts repeating

import numpy as np
from itertools import product
from tqdm import tqdm

with open('input.txt', 'r') as f:
    jets = f.readline().strip()

# create a play field, hopefully large enough
field = np.zeros((200000, 9), dtype=np.int0)
# create bottom floor and walls
field[0,:] = 2
field[:,0] = 2
field[:,8] = 2


# define shapes
shapes = []
# ####
shapes.append(np.ones(shape=(1, 4), dtype=np.int0))

# .#.
# ###
# .#.
shapes.append(np.ones(shape=(3, 3), dtype=np.int0))
shapes[1][0,0] = 0
shapes[1][0,-1] = 0
shapes[1][-1,0] = 0
shapes[1][-1,-1] = 0

# ..#
# ..#
# ###
shapes.append(np.ones(shape=(3, 3), dtype=np.int0))
shapes[2][1:,:2] = 0

# #
# #
# #
# #
shapes.append(np.ones(shape=(4, 1), dtype=np.int0))

# ##
# ##
shapes.append(np.ones(shape=(2, 2), dtype=np.int0))


# initialisation
height = 0 # height of the tower
# total_height = 0
shape = 0 # next shape to be added
add_new = True # start by adding a first shape
jet = 0
# keeping history of initial landscapes when a shape is introduced
# this should lead to detecting a repeated pattern
landscapes = []
heights = []
repetitions = {}

# let's try 500000 steps to identify the cycling pattern
print('generating data for pattern analysis')
for _ in tqdm(range(500000)):
    if add_new:
        # addintg new rock
        rock = shapes[shape % 5]        
        pos = [height+4, 3]
        # detect empty space below the rock:
        depth = []
        for col in range(1, 8):
            y = pos[0]-1
            while field[y, col] == 0:
                y -= 1
            depth.append(pos[0]-1-y)
        # save current "profile" and height
        depth = '-'.join(str(x) for x in [shape % 5]+depth+[jets[jet]])
        landscapes.append(depth)
        heights.append(height)
        if depth in repetitions:
            repetitions[depth] += 1
        else:
            repetitions[depth] = 1

        add_new = False
        shape += 1

        # rock added, try to apply jet
        if jets[jet] == '>' and pos[1]+rock.shape[1]<8:
            new_pos = field[pos[0]:pos[0]+rock.shape[0], pos[1]+1:pos[1]+1+rock.shape[1]]*rock
            if new_pos.sum() == 0:
                # can be moved
                pos[1] += 1
        elif jets[jet] == '<' and pos[1]>1:
            new_pos = field[pos[0]:pos[0]+rock.shape[0], pos[1]-1:pos[1]-1+rock.shape[1]]*rock
            if new_pos.sum() == 0:
                # can be moved
                pos[1] -= 1
        jet = (jet+1) % len(jets)        
    else:
        # trying to move a rock down
        new_pos = field[pos[0]-1:pos[0]-1+rock.shape[0], pos[1]:pos[1]+rock.shape[1]]*rock
        if new_pos.sum() > 0:
            # position is occupied -> becoming fixed and adding a new shape
            add_new = True
            for (i, j) in product(range(rock.shape[0]), range(rock.shape[1])):
                x = pos[0] + i
                y = pos[1] + j
                field[x, y] = min(1, rock[i, j]+field[x, y])
            # update height of the rock
            height = max(height, pos[0]+rock.shape[0]-1)
            # print('becomes static')
        else:
            # move rock 1 step down
            pos[0] -= 1
            # rock moved, try to apply jet
            if jets[jet] == '>' and pos[1]+rock.shape[1]<8:
                new_pos = field[pos[0]:pos[0]+rock.shape[0], pos[1]+1:pos[1]+1+rock.shape[1]]*rock
                if new_pos.sum() == 0:
                    # can be moved
                    pos[1] += 1
            elif jets[jet] == '<' and pos[1]>1:
                new_pos = field[pos[0]:pos[0]+rock.shape[0], pos[1]-1:pos[1]-1+rock.shape[1]]*rock
                if new_pos.sum() == 0:
                    # can be moved
                    pos[1] -= 1
            jet = (jet+1) % len(jets)

# zero's entry is at the beginning -> before any rock falls
rocks = 2022
rocks = 1000000000000
initial = max([i for i, p in enumerate(landscapes) if repetitions[p]==1])
print(f'number of initial rocks before repeating starts: {initial}')
print(f'height of initial rocks before repeating starts: {heights[initial]}')
repeating = landscapes[initial+1:]
# try to search for repeating pattern; maximum pattern length = 10000
for length in range(1, 10000):
    if repeating[0:length] == repeating[length:2*length]:
        break
print(f'length of repeating pattern: {length}')
height_repeating = heights[length+initial] - heights[initial]
print(f'height of repeating pattern: {height_repeating}')
number_repeating = (rocks-initial) // length
print(f'number of repeating patterns: {number_repeating}')
remainder = (rocks-initial) % length
print(f'number of rocks out-of-cycle: {remainder}')
height_remainder = heights[initial+remainder] - heights[initial]
print(f'total height of the tower: {heights[initial]+number_repeating*height_repeating+height_remainder}')