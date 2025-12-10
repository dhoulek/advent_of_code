import numpy as np
from tqdm import tqdm

# Read all 3D points from the input file
points = []
with open('input.txt') as f:
    for l in f.readlines():
        # Each line contains "x,y,z"
        points.append([int(x) for x in l.strip().split(',')])

points = np.array(points)

# Construct the full NxN matrix of Euclidean distances between points.
# dist_matrix[i][j] = distance between points[i] and points[j].
# This is O(N^2) both in time and memory.
dist_matrix = np.array([[np.linalg.norm(p - q) for q in points] for p in points])

# Flatten all distances, remove duplicates using set(), sort them,
# and skip the zero distances on the diagonal.
dists = sorted(list(set(dist_matrix.flatten())))[1:]

# Each point starts as its own circuit, labeled by its own index.
# circuits[i] stores the "circuit ID" for point i.
circuits = np.array([i for i in range(len(points))])

# Debug output: checks if all pairwise distances are unique.
# This is condition for the below code to work.
print(f'All distances unique? {len(dists) == int((len(points) * (len(points) - 1)) / 2)}')

# Iterate over all distances in increasing order.
# tqdm shows a progress bar.
counter = tqdm(dists)

for d in counter:
    # Show the number of current circuits in tqdm's status line.
    counter.set_description(f'Current number of circuits: {len(set(circuits))}')
    
    # Find all index pairs (i, j) whose distance equals this exact value.
    # Note: float equality can be unreliable, but works for your data.
    i, j = np.where(dist_matrix == d)[0]

    # If i and j belong to different circuits, merge them.
    if circuits[i] != circuits[j]:
        # All points currently in j's circuit get relabeled to i's circuit.
        for_merge = np.where(circuits == circuits[j])
        circuits[for_merge] = circuits[i]

    # Stop early if all points belong to the same circuit.
    if len(set(circuits)) == 1:
        break

# Output: multiply X-coordinates of the last merged pair (i, j).
# points[i][0] is the X coordinate of point i.
print(f'Distance to wall: {points[i][0] * points[j][0]}')