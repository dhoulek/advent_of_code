# Advent of Code 2024 - Day 12, Part 1
# Solution to calculate the total price of fencing required for regions of plants in a field.
# Each region consists of connected plots with the same plant type.
# The price is calculated based on the perimeter (fence) and size of each region.

import cmath  # Import the cmath module for handling complex numbers (used for grid positions).

# Parse the input file and represent the field as a dictionary.
field = dict()  # Stores the grid positions and their corresponding plant type.
with open('input.txt', 'r') as f:
    # Read the input file line by line and construct the field grid.
    for y, l in enumerate(f.readlines()):  # y is the line number (row index), l is the line content.
        for x, c in enumerate(l.strip()):  # x is the character index (column), c is the character.
            field[x + y * 1j] = c  # Use complex numbers (x + y*1j) to represent grid positions.

# Initialize variables for processing regions.
to_assign = list(field.keys())  # List of all positions that have not been assigned to a region.
regions = []  # List to store identified regions of connected plots.

# Identify all connected regions of the same plant type in the field.
while len(to_assign) > 0:
    c = field[to_assign[0]]  # Get the plant type at the first unassigned position.
    region = []  # List to store all positions belonging to the current region.
    check_nieghbors = [to_assign[0]]  # Queue to check neighbors of the current position.
    to_assign.pop(0)  # Remove the current position from unassigned positions.

    # Perform a breadth-first search (BFS) to find all connected plots of the same plant type.
    while len(check_nieghbors) > 0:
        pos = check_nieghbors[0]  # Take the first position to process.
        check_nieghbors.pop(0)  # Remove it from the queue.
        region.append(pos)  # Add the position to the current region.

        # Check neighboring positions (up, down, left, right).
        for delta in [-1, 1, -1j, 1j]:  # Complex number deltas to navigate the grid.
            if (pos + delta in to_assign) and field[pos + delta] == c:
                # If the neighbor is unassigned and has the same plant type, add it to the queue.
                to_assign.remove(pos + delta)
                check_nieghbors.append(pos + delta)

    # Append the identified region along with the plant type to the regions list.
    regions.append(dict(region=region, plant=c))

# Calculate the total price for fencing based on the size and perimeter of each region.
price = 0  # Total price accumulator.
for r in regions:
    fence = 0  # Perimeter (fence) of the current region.
    for plot in r['region']:
        # Check all four neighbors of the current plot.
        for delta in [-1, 1, -1j, 1j]:
            if not plot + delta in r['region']:
                # If the neighboring position is outside the region, increase the fence count.
                fence += 1
    # The price for the current region is size of the region multiplied by its perimeter.
    price += len(r['region']) * fence
    # Optional debug print: Uncomment to see details of each region.
    # print(r['plant'], len(r['region']), fence, len(r['region']) * fence)

# Print the final total price for all regions.
print('Total price for fencing is:', price)