# Correct solution for the test case, but wrong for the real input. Not sure what is wrong here,
# I have spent already too much time with this.
# 
# Solution based on Dijkstra algorithm, working on two "subgraphs".

import numpy as np
import cmath

field = []
with open('input.txt', 'r') as f:
    for l in f.readlines():
        field.append(np.array([int(i) for i in list(l.strip())]))
field = np.array(field)
n, m = field.shape

# construct graph
graph = {}
dist = {}
prev = {}
queue = []
for j in range(n):
    for i in range(m):
        g0 = complex(j, i)
        h = {}
        for x in range(max(0, i-3), i):
            h[complex(j, x)] = sum(field[j, x:i])
        for x in range(i+1, min(m, i+4)):
            h[complex(j, x)] = sum(field[j, i+1:x+1])
        v = {}
        for y in range(max(0, j-3), j):
            v[complex(y, i)] = sum(field[y:j, i])
        for y in range(j+1, min(n, j+4)):
            v[complex(y, i)] = sum(field[j+1:y+1, i])
        graph[g0] = [h, v]
        dist[g0] = [1e30, 1e30]
        prev[g0] = [[], []]
        queue.append(g0)

# starting node
dist[complex(0, 0)] = [0, 0]
prev[complex(0, 0)] = [[None], [None]]
queue = set(queue)

def find_next():
    n = None
    min_dist = 1e30
    for m in queue:
        if min(dist[m]) < min_dist:
            min_dist = min(dist[m])
            n = m
    return n

def print_dist():
    format_dist = lambda d: min(d) if min(d)<1e4 else -1
    
    d = []
    for j in range(n):
        d.append(np.array([format_dist(dist[complex(j, i)]) for i in range(m)]))
    print(np.array(d))
    
pair = lambda z: (int(z.real), int(z.imag))
        
# Dijkstra
while len(queue)>0:
    u = find_next()
    queue.remove(u)
    
    # we can go horizontal if we arrived vertical
    if len(prev[u][1]) > 0:
        check = [v for v in graph[u][0] if v in queue]
        for v in check:
            alt = dist[u][1] + graph[u][0][v]
            if alt <= dist[v][0]:
                dist[v][0] = alt
                prev[v][0] = [u]
    # we can go vertical if we arrived horizontal
    if len(prev[u][0]) > 0:
        check = [v for v in graph[u][1] if v in queue]
        for v in check:
            alt = dist[u][0] + graph[u][1][v]
            if alt < dist[v][1]:
                dist[v][1] = alt
                prev[v][1] = [u]

print_dist()