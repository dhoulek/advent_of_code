import re

names = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
positions = ['a2', 'd2',
             'a1', 'c1',
             'b1', 'c2',
             'b2', 'd1']

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
    upper = list('.#.#.#.')
    lower = list('.#.#.#.')
    for i, a in enumerate(positions):
        if re.match('[a-d]', a[0]):
            pos = positions_for_printing[a[0]]
            t = names[i]
            if int(a[1:]) == 1:
                upper[pos] = t
            else:
                lower[pos] = t
    return ''.join(upper), ''.join(lower)

def print_configuration(positions):
    print('#############')
    print(f'#{get_hallway(positions)}#')
    upper, lower = get_rooms(positions)
    print(f'###{upper}###')
    print(f'  #{lower}#  ')
    print('  #########  ')
    
def is_finished(i, positions):
    finished = False
    if names[i] == positions[i][0].upper():
        if int(positions[i][1:]) == 2:
            finished = True
        else:
            if i%2 == 0:
                finished = is_finished(i+1, positions)
            else:
                finished = is_finished(i-1, positions)
    return finished
    
def get_next_moves(positions):
    hallway = list(get_hallway(positions))
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
    min_energy = int(1e10)
    done = True
    for i in range(len(positions)):
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
                level = 2
                for o in range(len(positions)):
                    if o != i:
                        if positions[o][0] == a.lower():
                            if names[o] != a:
                                # other type in this room --> cannot enter
                                room_ready = False
                            else:
                                # already one correct in
                                level = 1
                if free and room_ready:
                    next = f'{a.lower()}{level}'
                    energy = energies[a]*(dist+level)
                    # print(pos, a, positions[i], next, energy, free, room_ready)
                    next_pos = positions.copy()
                    next_pos[i] = next
                    min_energy = min(min_energy, get_next_moves(next_pos)+energy)
            else:
                # amphipod in wrong room
                level = int(positions[i][1:])
                room = positions[i][0]
                if level == 2:
                    # check if above free
                    free = True
                    for o in range(len(positions)):
                        if o != i:
                            if positions[o][0] == room:
                                free = False
                if level == 1 or (level ==2 and free):
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
                                min_energy = min(min_energy, get_next_moves(next_pos)+energy)
    if done:
        return 0
    else:
        return min_energy
    

print('test case:')
positions = ['a2', 'd2',
             'a1', 'c1',
             'b1', 'c2',
             'b2', 'd1']
print_configuration(positions)
min_energy = get_next_moves(positions)
print(f'minimum energy is: {min_energy}')
print('')

print('puzzle input:')
positions = ['a1', 'd1',
             'c2', 'd2',
             'a2', 'c1',
             'b2', 'b1']
print_configuration(positions)
min_energy = get_next_moves(positions)
print(f'minimum energy is: {min_energy}')
print('')