pipes = {}
with open('test.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split(' ')
        valve = line[1]
        rate = int(line[4].split('=')[1][:-1])
        tunnels = [i.split(',')[0] for i in line[9:]]
        pipes[valve] = {'rate': rate, 
                        'tunnels': tunnels}
senseful_valves = set([v for v in pipes if pipes[v]['rate']>0])
print('valves which make sense to open:', senseful_valves)

def get_release(open_valves):
    return sum([pipes[v]['rate'] for v in open_valves])

def next_step(minute, position, open_valves):
    this_minute = get_release(open_valves)
    if minute < 30:        
        # check if there is actually anything that still could be opened
        if len(open_valves)<len(senseful_valves):
            if position not in open_valves and pipes[position]['rate'] > 0:
                # open valve
                # print(f'{minute}:  + opening {position}; opened valves in this minute: {open_valves}')                
                return this_minute + next_step(minute+1, position, open_valves+[position])
            else:
                # move through tunnel
                release = 0
                for n in pipes[position]['tunnels']:
                    # try all other tunnels
                    # print(f'{minute}: -> going to {n}; opened valves in this minute: {open_valves}')
                    release = max(release, next_step(minute+1, n, open_valves))
                return this_minute + release
        else:
            # last minute, return release of all opened valves
            print(f'{minute}: <> all valves are opened; opened valves in this minute: {open_valves}')
            return (30-minute+1)*this_minute
    else:
        # last minute, return release of all opened valves
        print(f'{minute}: ** last minute; opened valves in this minute: {open_valves}')
        return this_minute

print(next_step(10, 'AA', []))