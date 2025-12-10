import numpy as np

# Read all 3D points from the input file
points = []
with open('input.txt') as f:
    for l in f.readlines():
        # Each line is "x,y,z", convert to integers
        points.append([int(x) for x in l.strip().split(',')])

points = np.array(points)

# Build full pairwise distance matrix between all points.
# dist_matrix[i][j] = Euclidean distance between point i and point j.
# Note: This is O(N^2) and uses Python loops → slow for large inputs.
dist_matrix = np.array([[np.linalg.norm(p - q) for q in points] for p in points])

# Extract all unique distances, flattened.
# Convert to a set to remove duplicates, sort them, skip the zero distance.
# dists[i] is now the i-th smallest nonzero distance in the whole dataset.
dists = sorted(list(set(dist_matrix.flatten())))[1:]

# Initially, each point is in its own circuit.
# circuits[i] = label ID of the circuit containing point i.
# This serves as a simple union–find, but merging is done via relabeling arrays.
circuits = np.array([i for i in range(len(points))])

# Debug output: check whether all distances were unique (condition for the successful 
# evalution of the code).
print(f'All distances unique? {len(dists) == int((len(points) * (len(points) - 1)) / 2)}')

# Merge the closest 1000 pairs.
for d in dists[:1000]:
    # Find indices (i, j) where the distance equals this exact distance value.
    # WARNING: float equality comparisons can be risky due to precision.
    i, j = np.where(dist_matrix == d)[0]

    # If they are in different circuits, merge them
    if circuits[i] != circuits[j]:
        # All points currently in j's circuit get relabeled to i's circuit
        for_merge = np.where(circuits == circuits[j])
        circuits[for_merge] = circuits[i]

# Count how many distinct circuit labels remain
print(f'Number of circuits: {len(set(circuits))}')

# Compute sizes of each circuit (number of points with the same label)
lengths = sorted(
    [len(np.where(circuits == c)[0]) for c in set(circuits)],
    reverse=True
)

print(f'Length of circuits: {lengths}')

# Multiply the sizes of the 3 largest circuits
print(f'Product of three largest circuits: {np.prod(lengths[:3])}')