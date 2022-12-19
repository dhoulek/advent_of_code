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


# print(field[:10, :])

# for s in shapes:
#     print("")
#     print(s)
    
def print_field(n):
    f = field[:n, :].copy()
    for (i, j) in product(range(rock.shape[0]), range(rock.shape[1])):
        f[i+pos[0], j+pos[1]] = 5*rock[i, j]
    print()
    print(f'rock number: {shape}')
    for l in reversed(range(n)):
        line = ''.join([str(x) for x in f[l, :]])
        line = line.replace('0', '.')
        line = line.replace('2', '+')
        line = line.replace('1', '#')
        line = line.replace('5', '@')
        print(line)

# initialisation
height = 0 # height of the tower
# total_height = 0
shape = 0 # next shape to be added
add_new = True # start by adding a first shape
jet = 0
# keeping history of initial landscapes when a shape is introduced
# this should lead to detecting a repeated pattern
landscapes = [[] for _ in shapes]
heights = []

for _ in tqdm(range(5000000)):
    if add_new:
        # if height > 11500:
        #     total_height += 10000
        #     height -= 10000
        #     # move play field by 10000 positions
        #     f = field.copy()
        #     field = np.zeros((12000, 9), dtype=np.int0)            
        #     field[0:1800,:] = f[10000:11800,:]
        #     print(f'current height: {height+total_height}')
        #     print(f'adding a rock number: {shape}')

        # addintg new rock
        rock = shapes[shape % 5]        
        pos = [height+4, 3]
        # saving height when adding this rock
        heights.append(height)#+total_height)        
        # detect empty space below the rock:
        depth = []
        for col in range(1, 8):
            y = pos[0]-1
            while field[y, col] == 0:
                y -= 1
            depth.append(pos[0]-1-y)
        depth = '-'.join(str(x) for x in depth)
        if shape in [155, 156, 157, 1874, 1875, 1876, 1877]:
            print(shape, depth)                
        # check for the same profile AND jet state        
        if depth in landscapes[shape % 5]:
            lasttime_shape = landscapes[shape % 5].index(depth)
            lasttime = lasttime_shape*5 + shape % 5
            if shape % len(jets) == lasttime % len(jets):
                print(shape, lasttime)
                print('FOUND a repeating pattern!')
                break
            # print('FOUND a repeating pattern!')
            # break
        else:
            landscapes[shape % 5].append(depth)

        add_new = False
        shape += 1
        # print_field(height + 10)
        # input()
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
        # r.set_description(f'rock: {shape}; height: {total_height+height}')
        # print(f'jet number: {jet} {len(jets)}')
        # print()
        # print_field(height)
        # print()
        # if shape == 2022:
        #     break
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
            # print(f'jet number: {jet} {len(jets)}')


# don't forget that very first rock has index 0!            
lasttime_shape = landscapes[shape % 5].index(depth)
lasttime = lasttime_shape*5 + shape % 5
last_height = heights[lasttime]
print(f'current rock: {shape+1}') 
print(f' landscape it sees: {depth}')
print(f'last time this rock saw the same landscape {lasttime_shape}')
print(f' landscape at that time: {landscapes[shape % 5][lasttime_shape]}')
print(f' at that time, if was a stone: {lasttime+1}')
print(f' height at that time: {last_height}')
print(f' height now: {heights[-1]}')
print(f' height of the period: {heights[-1]-last_height}')
print(f'initial {lasttime} rocks added up to {last_height}')
print(f'every: {shape-lasttime} rocks correspond to {heights[-1]-last_height} height increase')
num_rocks = 1000000000001
remaining = num_rocks-lasttime-1
period = shape-lasttime
repetitions = remaining // period
print(f'{num_rocks} = {lasttime+1} + {period}*{repetitions} + {remaining % period}')
remaining_height = heights[lasttime + remaining % period] - last_height
total_height = heights[lasttime + remaining % period] + (heights[-1]-last_height)*repetitions
print(f'{total_height} = {last_height} + {heights[-1]-last_height}*{repetitions} + {remaining_height}')