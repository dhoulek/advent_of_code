import numpy as np
import cmath

# Set part2 to True if solving for part 2 of the problem
part2 = True

# Initialize set to store corner points
corners = set()

# Initialize starting position
pos = np.array([0, 0])

# Define directions and their corresponding vectors
dirs = {
    'R': np.array([1, 0]),
    'D': np.array([0, -1]),
    'L': np.array([-1, 0]),
    'U': np.array([0, 1]),
}
dirs2 = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U',
}

# Read input from file
with open('input.txt', 'r') as f:
    for l in f.readlines():
        dir, length, color = l.strip().split()
        length = int(length)
        if part2:
            # Parse instructions from the color information for part 2
            color = color[1:-1]
            dir = dirs2[color[-1]]
            length = int(color[1:-1], 16)
        pos = pos + length * dirs[dir]
        corners.add(complex(*pos))

# Extract x and y grid from corner points
x, y = [], []
for p in corners:
    x.append(p.real)
    y.append(p.imag)
x = list(sorted(list(set(x))))
y = list(sorted(list(set(y))))
m, n = len(x), len(y)

# Initialize lists to store rectangles and area
rectangles = []
area = 0

# Iterate over rows
for j in range(n - 1):
    rect = []
    out = True
    # Iterate over columns
    for xx in x:
        z = complex(xx, y[j])
        if z in corners:
            if out:
                # Starting new rectangle
                LL = z
                out = False
            else:
                # Ending the current rectangle
                LR = z
                out = True
                # Find upper corners
                UL = complex(LL.real, y[j + 1])
                UR = complex(LR.real, y[j + 1])
                # Update corner set
                if UL in corners:
                    corners.remove(UL)
                else:
                    corners.add(UL)
                if UR in corners:
                    corners.remove(UR)
                else:
                    corners.add(UR)
                # Add rectangle to list and update area
                rect.append([LL.real, LR.real])
                area += abs((LR - LL + 1) * (abs(UR - LR) + 1))
    rectangles.append(rect)
    if not out:
        # Check if the last rectangle continues to the next row
        print(out)

# Correction for overlapping rectangles
for j in range(n - 2):
    for a, b in rectangles[j]:
        # Find overlaps with upper row
        for A, B in rectangles[j + 1]:
            A = max(A.real, a)
            B = min(B.real, b)
            if A <= B:
                area -= (B + 1 - A)

# Print results
if part2:
    print('Part 2')
else:
    print('Part 1')
print(f'Volume of the lava reservoir: {int(area)}')