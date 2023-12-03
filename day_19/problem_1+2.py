import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import time

cost_matrices = {}
# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split(':')
        i = int(line[0].split()[-1])
        line = line[1].split('.')
        cost = np.zeros((4, 4), dtype=np.int0)
        cost[0][0] = int(line[0].split()[-2])
        cost[1][0] = int(line[1].split()[-2])
        cost[2][0] = int(line[2].split()[-5])
        cost[2][1] = int(line[2].split()[-2])
        cost[3][0] = int(line[3].split()[-5])
        cost[3][2] = int(line[3].split()[-2])
        cost_matrices[i] = cost

# print(cost_matrices)

# working with an assumption that only maximum one robot is created each minite
upgrade_all = [True]*4
		

def play_minute(robots, resources, step, upgrades):
    global maximum_geodes
    if step > 1:
        # not the last minute        
        # estimate maximum number of geodes if no more geode robots are created
        no_more_robots = resources[3] + robots[3] * step
        if no_more_robots > maximum_geodes:
            maximum_geodes = no_more_robots
            # print("- new best:", maximum_geodes)
        # VERY optimistic estimate: every minute is the number of created geode robots 
        # increased by one
        max_optimistic = no_more_robots + (step-1)*(step)//2
        if (max_optimistic <= maximum_geodes):
            # this most optimistic scenario will not bring any better result
            return
        # check robot by robot if enough resources for creation
        possible_upgrades = [bool(int(min(resources / costs[i]))) for i in range(4)]
        
        ##################################################################################
        # NOTE: originally, the 4 below if statements were elegantly implemented via for #
        # loop and a list of possible upgrades; however, the solution was ~100x slower!  #
        # the current implementation is inspired by Tobias :-) THANKS                    #
        ##################################################################################
        
        ##################################################################################
        # cost = np.dot(upgrade, costs) is FASTER than cost = np.dot(costs.T, upgrade)   #
        ##################################################################################
        
        # try geode robot
        if possible_upgrades[3] and upgrades[3]:
            upgrade = (0, 0, 0, 1)
            cost = np.dot(upgrade, costs)
            play_minute(robots+upgrade, resources-cost+robots, step-1, upgrade_all)
        # try obsidian robot
        if possible_upgrades[2] and upgrades[2]:
            upgrade = (0, 0, 1, 0)
            cost = np.dot(upgrade, costs)
            play_minute(robots+upgrade, resources-cost+robots, step-1, upgrade_all)
        # try clay robot
        if possible_upgrades[1] and upgrades[1]:
            upgrade = (0, 1, 0, 0)
            cost = np.dot(upgrade, costs)
            play_minute(robots+upgrade, resources-cost+robots, step-1, upgrade_all)
        # try ore robot, if still needed
        if possible_upgrades[0] and upgrades[0] and robots[0] < max_ore_robots:
            upgrade = (1, 0, 0, 0)
            cost = np.dot(upgrade, costs)
            play_minute(robots+upgrade, resources-cost+robots, step-1, upgrade_all)
        # try with no robot; next minute try to create only those, which couldn't
        # be created in this minute        
        play_minute(robots, resources+robots, step-1, [not i for i in possible_upgrades])
    else:
        # final minute, check the number of geodes cracked by the geode-cracking robots
        if resources[3]+robots[3] > maximum_geodes:
            maximum_geodes = resources[3]+robots[3]
            # print("- new best:", maximum_geodes)
            
print('-------- PART 1 ----------')        
quality = 0
for ID in cost_matrices.keys():
    print(f'solving ID: {ID}')
    costs = cost_matrices[ID]
    # start with 1 ore robot
    robots = np.array([1, 0, 0, 0])
    # start with nothing
    resources = np.array([0, 0, 0, 0])
    # keeping maximum number of cracked geodes for efficient pruning impossible branches
    maximum_geodes = -1
    # maximum ore robots needed (assumption: max 1 robot per minute!)
    max_ore_robots = max(costs[:, 0])
    # print(max_ore_robots)
    start = time.time()
    play_minute(robots, resources, 24, upgrade_all)
    end = time.time()
    quality += ID*maximum_geodes
    print(f'   geodes: {maximum_geodes}  quality level: {ID*maximum_geodes}  duration: {end-start:.3f}s')
print(f'total quality level: {quality}')

print()

print('-------- PART 2 ----------')
quality = 1
for ID in range(1, 4):
    print(f'solving ID: {ID}')
    costs = cost_matrices[ID]
    # start with 1 ore robot
    robots = np.array([1, 0, 0, 0])
    # start with nothing
    resources = np.array([0, 0, 0, 0])
    # keeping maximum number of cracked geodes for efficient pruning impossible branches
    maximum_geodes = -1
    # maximum ore robots needed (assumption: max 1 robot per minute!)
    max_ore_robots = max(costs[:, 0])
    # print(max_ore_robots)
    start = time.time()
    play_minute(robots, resources, 32, upgrade_all)
    end = time.time()
    quality *= maximum_geodes
    print(f'   geodes: {maximum_geodes}  quality level: {ID*maximum_geodes}  duration: {end-start:.3f}s')
print(f'total quality level: {quality}')
