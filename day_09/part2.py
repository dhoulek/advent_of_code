import numpy as np
from tqdm import tqdm

# Read all red-corner coordinates from input (each row "x,y")
corners = []
with open('input.txt') as f:
    for l in f.readlines():
        corners.append([int(x) for x in l.strip().split(',')])

# Build polygon edges from consecutive red tiles.
# The input forms a closed rectilinear polygon in order.
vertical_edges = []
horizontal_edges = []
for a, b in zip(corners, corners[1:] + corners[:1]):  # wrap around
    # Vertical edge: same x, varying y
    if a[0] == b[0]:
        # Store as [x, [y_low, y_high]]
        vertical_edges.append([a[0], sorted([a[1], b[1]])])

    # Horizontal edge: same y, varying x
    elif a[1] == b[1]:
        # Store as [y, [x_low, x_high]]
        horizontal_edges.append([a[1], sorted([a[0], b[0]])])

# ---------------------------------------------------------
# Check if the straight line segment between points a and b
# crosses any edge of the polygon. If it does, the rectangle
# diagonal or edge would leave the interior, making the
# rectangle invalid.
# 
# This ensures the entire rectangle lies inside the polygon.
# ---------------------------------------------------------
def check_edge_cross(a, b):
    # Compute axis-aligned bounding box of the segment a→b.
    # We check intersections only within this box.
    xmin = min(a[0], b[0])
    xmax = max(a[0], b[0])
    ymin = min(a[1], b[1])
    ymax = max(a[1], b[1])

    # ------------------------
    # Check intersections with all *horizontal* polygon edges.
    # A horizontal edge is: y = constant, between x-range e.
    # ------------------------
    for y, e in horizontal_edges:
        # Edge must be vertically between endpoints of the segment.
        if ymin < y < ymax:
            # If horizontal edge lies completely to left or right,
            # they cannot intersect.
            if e[0] >= xmax or e[1] <= xmin:
                continue
            else:
                # Overlapping ranges → crossing
                return True                   

    # -----------------------
    # Check intersections with all *vertical* polygon edges.
    # A vertical edge is: x = constant, between y-range e.
    # -----------------------
    for x, e in vertical_edges:
        # Edge must be horizontally between endpoints of the segment.
        if xmin < x < xmax:
            # If vertical edge lies entirely above or below,
            # they cannot intersect.
            if e[0] >= ymax or e[1] <= ymin:
                continue
            else:
                # Overlapping ranges → crossing
                return True

    # If no edges were crossed, the segment stays inside polygon.
    return False
        

# ---------------------------------------------------------
# Exhaustively test all pairs of red corners.
# A rectangle is axis-aligned since corners share x/u and y/v.
# The area is (Δx+1)*(Δy+1) because tiles are inclusive.
# ---------------------------------------------------------
max_area = 0
for i in tqdm(range(len(corners)-1)):
    a = corners[i]
    for b in corners[i+1:]:
        # Compute rectangular area quickly
        rect_area = (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)

        # Skip if this rectangle cannot beat current best
        if rect_area <= max_area:
            continue

        # Check if the diagonal a→b crosses the polygon boundary.
        # If it does NOT, the whole rectangle is inside.
        if not check_edge_cross(a, b):
            max_area = rect_area  # update best

print(f'The largest area of any rectangle: {max_area}')