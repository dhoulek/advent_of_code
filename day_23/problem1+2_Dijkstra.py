import re

def get_hallway(positions):
    hallway = list('...........')
    for i, a in enumerate(positions):
        if a[0] == 'h':
            pos = int(a[1:])
            t = names[i]
            hallway[pos] = t
    return ''.join(hallway)

def get_rooms(positions):
    positions_for_printing = {'a': 0,
                              'b': 2,
                              'c': 4,
                              'd': 6
                              }
    levels = [list('.#.#.#.') for i in range(int(len(names)/4))]
    for i, a in enumerate(positions):
        if re.match('[a-d]', a[0]):
            pos = positions_for_printing[a[0]]
            t = names[i]
            # print(a, int(a[1:])-1)
            levels[int(a[1:])-1][pos] = t
    return levels

def code_configuration(positions):
    code = get_hallway(positions)
    levels = get_rooms(positions)
    for l in levels:
        code += '|'
        code += ''.join([l[i] for i in [0,2,4,6]])
    return code
    
def print_configuration(positions):
    print('#############')
    print(f'#{get_hallway(positions)}#')
    levels = get_rooms(positions)
    print(f'###{"".join(levels[0])}###')
    for i in range(1, len(levels)):
        print(f'  #{"".join(levels[i])}#  ')
    print('  #########  ')
    
def is_finished(i, positions):
    finished = False
    this_level = int(positions[i][1:])
    if names[i] == positions[i][0].upper():
        finished = True
        for io, o in enumerate(positions):
            pos = o[0]
            level = int(o[1:])
            # print(o, positions[i], io, i, names[io] != names[i], level, this_level)
            if names[io] != pos.upper() and pos == positions[i][0] and level > this_level:
                finished = False
    # print(finished)
    return finished

positions_of_rooms = {'A': 2,
                      'B': 4,
                      'C': 6,
                      'D': 8
                    }
energies = {'A': 1,
            'B': 10,
            'C': 100,
            'D': 1000
            }


names = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D']

positions = ['a4', 'd4', 'd2', 'c3',
             'a1', 'c1', 'b3', 'c2',
             'b1', 'c4', 'b2', 'd3',
             'b4', 'd1', 'a2', 'a3']
positions = ['a2', 'd2', 'a3', 'a4',
             'a1', 'c1', 'b3', 'b4',
             'b1', 'c2', 'c3', 'c4',
             'b2', 'd1', 'd3', 'd4']
target = ['a1', 'a2', 'a3', 'a4',
          'b1', 'b2', 'b3', 'b4',
          'c1', 'c2', 'c3', 'c4',
          'd1', 'd2', 'd3', 'd4']

### TEST PART 1
# names = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
# positions = ['a2', 'd2',
#              'a1', 'c1',
#              'b1', 'c2',
#              'b2', 'd1']
# target = ['a1', 'a2',
#           'b1', 'b2',
#           'c1', 'c2',
#           'd1', 'd2']

### EASY TEST
# names = ['A', 'B', 'C', 'D']
# positions = ['d1',
#              'b1',
#              'c1',
#              'a1']
# target = ['a1',
#           'b1',
#           'c1',
#           'd1',]
print_configuration(positions)
# print(code_configuration(positions))

graph = {code_configuration(positions): [None, 0]}
explored = []
moves = [positions]
done = False
MAX_DEPTH = int(len(positions)/4)

while not done:
# for _ in range(10):
    # print(code_configuration(target) in graph.keys())
    # print(len(graph), len(moves))
    dist = [graph[code_configuration(m)][1] for m in moves]
    next_index = dist.index(min(dist))
    positions = moves.pop(next_index)
    # print(dist, next_index)
    explored.append(code_configuration(positions))
    print(dist[next_index], len(explored), len(moves))
    # print(code_configuration(positions), positions)
    this_node = code_configuration(positions)
    hallway = list(get_hallway(positions))
    done = True
    for i in range(len(positions)):
        # print(i, positions[i], is_finished(i, positions))
        if not is_finished(i, positions):
            done = False
            pos = int(positions[i][1:])
            a = names[i]
            if positions[i][0] == 'h':
                # amphipod is in the hallway
                if pos>positions_of_rooms[a]:
                    free = hallway[positions_of_rooms[a]:pos] == ['.']*(pos-positions_of_rooms[a])
                else:
                    free = hallway[pos+1:positions_of_rooms[a]+1] == ['.']*(positions_of_rooms[a]-pos)
                dist = abs(pos-positions_of_rooms[a])
                room_ready = True
                occupied = 0
                for o in range(len(positions)):
                    if o != i:
                        if positions[o][0] == a.lower():
                            if names[o] != a:
                                # other type in this room --> cannot enter
                                room_ready = False
                            else:
                                # already one correct in
                                occupied += 1
                if free and room_ready:
                    level = MAX_DEPTH-occupied
                    next = f'{a.lower()}{level}'
                    energy = energies[a]*(dist+level)
                    # print(pos, a, positions[i], next, energy, free, room_ready)
                    next_pos = positions.copy()
                    next_pos[i] = next
                    code = code_configuration(next_pos)
                    if code in graph.keys():
                        if graph[code][1] > graph[this_node][1]+energy:
                            graph[code] = [this_node, graph[this_node][1]+energy]
                    else:
                        graph[code] = [this_node, graph[this_node][1]+energy]
                    # if code not in explored:
                    if next_pos not in moves:
                        moves.append(next_pos)
            else:
                # amphipod in wrong room
                level = int(positions[i][1:])
                room = positions[i][0]
                # check if above free
                free = True
                for o in range(len(positions)):
                    other_room = positions[o][0]
                    other_level = int(positions[o][1:])
                    if  other_room == room and other_level < level:
                            free = False
                if free:
                    for final in range(len(hallway)):
                        if final not in positions_of_rooms.values():
                            pos = positions_of_rooms[positions[i][0].upper()]
                            if final>pos:
                                free_hallway = hallway[pos:final+1] == ['.']*(final-pos+1)
                            else:
                                free_hallway = hallway[final:pos+1] == ['.']*(pos-final+1)
                            if free_hallway:
                                dist = abs(pos-final)
                                next = f'h{final}'
                                energy = energies[a]*(dist+level)
                                # print(pos, a, positions[i], next, energy, level, dist, free, free_hallway)
                                next_pos = positions.copy()
                                next_pos[i] = next
                                code = code_configuration(next_pos)
                                if code in graph.keys():
                                    if graph[code][1] > graph[this_node][1]+energy:
                                        graph[code] = [this_node, graph[this_node][1]+energy]
                                else:
                                    graph[code] = [this_node, graph[this_node][1]+energy]
                                # if code not in explored:
                                if next_pos not in moves:
                                    moves.append(next_pos)

print(f'minumum energy: {graph[code_configuration(target)][1]}')