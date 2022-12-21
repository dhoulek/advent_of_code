import numpy as np
np.seterr(divide='ignore', invalid='ignore')
from itertools import product

cost_matrices = {}
with open('test.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split(':')
        i = int(line[0].split()[-1])
        line = line[1].split('.')
        cost = np.zeros((4, 4), dtype=np.int0)
        cost[0][0] = int(line[0].split()[-2])
        cost[1][0] = int(line[1].split()[-2])
        cost[2][0] = int(line[2].split()[-2])
        cost[2][1] = int(line[2].split()[-5])
        cost[3][0] = int(line[3].split()[-2])
        cost[3][2] = int(line[3].split()[-5])
        cost_matrices[i] = cost

print(cost_matrices)
		

def check_upgrades(resources, costs, robots, step):
    # check robot by robot for maximum number of upgrades
    max_upgrades = [int(min(resources / cost[i])) for i in range(4)]
    global maximum_geodes
    upgrades = []
    print('m', maximum_geodes, step, resources, max_upgrades)
    
    # estimate if no more geode robots are created
    no_more_robots = resources[3] + robots[3] * step
    if no_more_robots > maximum_geodes:
        maximum_geodes = no_more_robots
        print("- new best:", maximum_geodes)
    # VERY optimistic estimate: every minute is the number of created geode robotes 
    # increased by one
    max_optimistic = no_more_robots + step // cost[3,0]
    # print(24*25//cost.T[0].prod())
    # if (max_optimistic <= maximum_geodes):
        # no need to check anything - we cannot beat the current maximum
        # return upgrades
    for upgrade in product(*[reversed(range(max_upgrades[i]+1)) for i in reversed(range(4))]):
        # check if enough resources available
        upgrade = upgrade[::-1]
        # print(step, '.')
        c = np.dot(costs.T, upgrade)
        if sum(c <= resources) == 4:
            upgrades.append(upgrade)
        # print(upgrades)
    return upgrades


def play_minute(robots, resources, costs, step):    
    global maximum_geodes
    # print(step)
    print('--', step, resources, robots)
    if step > 0:
        upgrades = check_upgrades(resources, costs, robots, step)
        # print(step, len(upgrades))
        for upgrade in upgrades:
            # print(upgrade)
            cost = np.dot(costs.T, upgrade)
            play_minute(robots+upgrade, resources-cost+robots, costs, step-1)
        # return the best you can do in the future + number of geodes cracked by the currently
        # existing geode-cracking robots
        # if len(geodes) > 0:
        #     return robots[3] + max(geodes)
        # else:
        #     return robots[3]
    else:
        # print('.', resources)
        # final minute, return number of geodes cracked by the number of geode-cracking robots
        if resources[3]+robots[3] > maximum_geodes:
            maximum_geodes = resources[3]+robots[3]
            print("- new best:", maximum_geodes)
            
        

costs = cost_matrices[1]
# start with 1 ore robot
robots = np.array([1, 0, 0, 0])
# start with nothing
resources = np.array([0, 0, 0, 0])
# keeping maximum number of cracked geodes for efficient pruning impossible branches
maximum_geodes = -1
print(cost)
# print(play_minute(robots, [24, 65, 3, 0], costs, 2))
# print(play_minute(robots, [24, 65, 3, 0], costs, 2))
print(play_minute(robots, resources, costs, 2))


        
        # print(cost)
        # print(np.dot(cost.T, [1,0,1,0]))