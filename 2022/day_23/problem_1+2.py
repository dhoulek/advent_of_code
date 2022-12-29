import numpy as np

# read inputs
elves = []
i = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        for j, c in enumerate(line):
            if c == '#':
                elves.append([i, j])
        i += 1


# count number of empty squares
def get_number_empty(elves):
    # get min-max positions for estimating smallest rectangle
    elves = np.array(elves)
    # area of the rectangle
    area = (max(elves[:,0])-min(elves[:,0])+1)*(max(elves[:,1])-min(elves[:,1])+1)
    # number of empty tiles is area - # of elves
    return area-len(elves)


NN = [[[-1, -1], [-1,  0], [-1,  1]],
      [[ 1, -1], [ 1,  0], [ 1,  1]],
      [[ 1, -1], [ 0, -1], [-1, -1]],
      [[ 1,  1], [ 0,  1], [-1,  1]]
      ]

def product(l):
    p = 1
    for i in l:
        p *= i
    return p

def get_proposal(elves, turn):
    # shuffle nearest neighbours
    nn = [NN[(i+turn)%4] for i in range(4)]
    # print(nn[0][1])
    moving = False
    proposals = []
    for e in elves:
        # get number of neighbours in each of the fours considered directions
        neighbours = [sum([contains([e[0]+n[0], e[1]+n[1]], elves) for n in nn_set]) 
                      for nn_set in nn]
        # print(e, neighbours)
        if sum(neighbours) == 0 or product(neighbours)>0:
            # static elf!
            proposals.append(e)
        else:
            # get proposal for new position!
            moving = True
            for i, n in enumerate(neighbours):
                if n == 0:
                    # free direction
                    proposals.append(tuple([e[0] + nn[i][1][0], e[1] + nn[i][1][1]]))
                    break
    return proposals, moving


def contains(e, l):
    # check if e is in l
    indices = [i for i, x in enumerate(l) if tuple(x) == tuple(e)]
    return len(indices) >= 1
    
def check_duplicate(e, l):
    # check if e is more than once in l
    indices = [i for i, x in enumerate(l) if tuple(x) == tuple(e)]
    return len(indices)>1

def print_elves(elves, ymin=0, ymax=5, xmin=0, xmax=4):
    board = np.zeros(((ymax-ymin)+1, (xmax-xmin)+1), dtype=np.int0)
    for e in elves:
        if (ymin <= e[0] <= ymax) and (xmin <= e[1] <= xmax):
            board[tuple([e[0]-ymin, e[1]-xmin])] = 1
    for line in board:
        print(''.join(['.' if x == 0 else '#' for x in line]))
    

# print_elves(elves, xmax=13, ymax=11)
step = 0
moving = True
while moving:
    proposals, moving = get_proposal(elves, step)
    step += 1
    print(f'step: {step}')
    if moving:
        # check for duplicates; if singular proposal, update the position, otherwise
        # remain in the old position
        for i, n in enumerate(proposals):
            if not check_duplicate(n, proposals):
                elves[i] = n
        # print(elves)
        # print_elves(elves, xmax=13  , ymax=11)        
        print(f'empty tiles: {get_number_empty(elves)}, number of elves: {len(elves)}')
    else:
        print('DONE')