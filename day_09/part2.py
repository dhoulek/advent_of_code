# Advent of Code 2024, Day 8, Part 2 Solution
# This script processes a disk structure to optimize file positions,
# ensuring files are moved into earlier available spaces when possible,
# and calculates a control checksum based on the final arrangement.

from tqdm import tqdm  # Progress bar utility for iterations.

# Initialize the disk as an empty list.
disk = []

# Read input data from the file.
# Each line contains alternating counts of file sizes and gaps.
with open('input.txt', 'r') as f:
    l = [int(c) for c in f.readline().strip()]  # Convert the input line into a list of integers.
    length = sum(l)  # Calculate the total length of the disk.

# Initialize position and lists for files and spaces.
pos = 0  # Current position pointer.
files = []  # List to store file metadata (position and length).
spaces = []  # List to store gap metadata (position and length).
file = True  # Flag to toggle between file sizes and gaps.

# Parse the input data into `files` and `spaces`.
for i in l:
    if file:  # If `file` is True, add the file's position and length to the `files` list.
        files.append(dict(pos=pos, len=i))
    else:  # If `file` is False, add the gap's position and length to the `spaces` list.
        if i > 0:  # Only add gaps that have a positive length.
            spaces.append(dict(pos=pos, len=i))
    pos += i  # Update the position pointer by the current segment's length.
    file = not file  # Toggle the `file` flag.

# Move files into earlier available spaces if possible.
for fi in tqdm(range(len(files) - 1, -1, -1)):  # Iterate over files in reverse order.
    f = files[fi]  # Get the current file's metadata.
    for si, s in enumerate(spaces):  # Iterate over available spaces.
        # Check if the space is large enough to hold the file and is positioned earlier.
        if (s['len'] >= f['len']) and (s['pos'] < f['pos']):
            # Update the file's position to the start of the space.
            files[fi]['pos'] = s['pos']
            # Reduce the space's length by the file's length.
            spaces[si]['len'] -= f['len']
            # Update the space's starting position.
            spaces[si]['pos'] += f['len']
            break  # Stop searching for a space for the current file.

# Construct the final disk layout.
disk = ['.'] * length  # Initialize the disk with gaps ('.').
for id, f in enumerate(files):  # Iterate over files and their metadata.
    # Fill the disk with the file ID for the file's length starting at its position.
    for p in range(f['pos'], f['pos'] + f['len']):
        disk[p] = id

# Calculate the control checksum.
# The checksum is the weighted sum of file IDs multiplied by their positions.
checksum = sum([p * disk[p] for p in range(len(disk)) if not disk[p] == '.'])

# Output the control checksum.
print(f'Control checksum is: {checksum}')