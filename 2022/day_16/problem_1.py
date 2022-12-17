import numpy as np

pipes = {}
with open('test.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split(' ')
        valve = line[1]
        rate = int(line[4].split('=')[1][:-1])
        tunnels = [i.split(',')[0] for i in line[9:]]
        pipes[valve] = {'rate': rate, 
                        'tunnels': tunnels}

all_valves = tuple(pipes.keys())
print('all valves:', all_valves)
senseful_valves = set([v for v in pipes if pipes[v]['rate']>0])
print('valves which make sense to open:', senseful_valves)

# create a distance matrix
dist = np.array([None]*len(all_valves)**2).reshape(len(all_valves), len(all_valves))
for v1 in all_valves:
    for v2 in pipes[v1]['tunnels']:
        dist[all_valves.index(v1), all_valves.index(v2)] = 1
# keep constructing paths with intermediate node
new_connection = True
while new_connection:
    new_connection = False
    # dist[i,j] = dist[i,l] + dist[l,j] = dist[i,l] + dist[j,l]
    for line in range(len(all_valves)):
        for i in range(len(all_valves)-1):
            for j in range(i+1, len(all_valves)):
                if dist[line, i] != None and dist[line, j] != None:
                    if dist[i, j] == None or dist[i, j] > dist[line, i] + dist[line, j]:
                        dist[i, j] = dist[line, i] + dist[line, j]
                        dist[j, i] = dist[line, i] + dist[line, j]
                        new_connection = True

np.set_printoptions(threshold=np.inf)
print(dist)

# evaluate path
def eval_path(time, path):
    return sum([(30-t)*pipes[n]['rate'] for t, n in zip(time, path)])

# construct all possible paths through all "senseful" nodes -- nodes with
# rates > 1; visiting each node takes 1 minute (needed to open the valve).
# maximum travel time (including opening valves) is 30 minutes
to_visit = senseful_valves
time = [0]
path = ['AA']

max_relief = 0
best_path = []
best_time = []

def make_move(time, path, to_visit):
    global max_relief
    global best_path
    global best_time
    current = path[-1]
    now = time[-1]
    if len(to_visit) > 0 and now < 30:
        for n in to_visit:
            # length + 1 for opening
            duration = dist[all_valves.index(current), all_valves.index(n)] + 1
            # print(duration)
            make_move(time+[min(duration+now, 30)], path+[n], to_visit-{n})
    else:
        # print(path, time)
        relief = eval_path(time, path)
        if relief > max_relief:
            max_relief = relief
            best_path = path
            best_time = time
        
make_move(time, path, to_visit)
print(f'maximum relief is {max_relief}')
print(f'this is obtained for valves {best_path}')
print(f' relieving pressure from times {best_time}')


