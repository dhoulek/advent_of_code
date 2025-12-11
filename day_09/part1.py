import numpy as np

# Read input: each line is "x,y"
# These are all the red tiles. Part 1 only cares about rectangles
# made from two red tiles -- with no restriction on what tiles lie inside.
corners = []
with open('input.txt') as f:
    for l in f.readlines():
        corners.append([int(x) for x in l.strip().split(',')])

# Convert to a NumPy array for convenience
corners = np.array(corners)

areas = []

# ---------------------------------------------------------
# Check every pair of red tiles.
#
# In part 1, *any* rectangle formed by picking two opposite corners is allowed.
# There is no restriction about interior tiles — all tiles are allowed.
#
# The rectangle formed by corners A(x1,y1) and B(x2,y2) has width = |x1−x2|+1
# and height = |y1−y2|+1, because tile coordinates are inclusive.
#
# area = (|x1−x2|+1) * (|y1−y2|+1)
# ---------------------------------------------------------
for i, a in enumerate(corners[:-1]):
    for b in corners[i+1:]:
        # Compute the inclusive-area of the axis-aligned rectangle between a and b
        area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        areas.append(area)

# The largest rectangle area found among all red tile pairs
print(f'The largest area of any rectangle: {np.max(areas)}')