import numpy as np
from itertools import product

with open('input.txt', 'r') as f:
    jets = f.readline().strip()

# create a play field, hopefully large enough
field = np.zeros((10000, 9), dtype=np.int0)
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


print(field[:10, :])

for s in shapes:
    print("")
    print(s)
    
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
shape = 0 # next shape to be added
add_new = True # start by adding a first shape
jet = 0

for _ in range(50000):
    if add_new:
        # addintg new rock
        
        rock = shapes[shape % 5]
        shape += 1
        pos = [height+4, 3]
        add_new = False
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
        print(f'current height: {height}')
        print(f'adding a rock number: {shape}')
        # print(f'jet number: {jet} {len(jets)}')
        print()
        # print_field(height)
        # print()
        if shape == 2023:
            break
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