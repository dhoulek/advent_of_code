# Advent of Code 2024, Day 8, Part 1 Solution
# This script simulates a disk-based data structure, processes it by removing certain elements,
# and calculates a control checksum based on the remaining data.

# Initialize the disk as an empty list.
disk = []

# Read input data from the file.
# Each line in the input represents file sizes (integers) alternated with gaps (represented by '.').
with open('input.txt', 'r') as f:
    l = [int(c) for c in f.readline().strip()]  # Convert the input line into a list of integers.

# Populate the disk using the input data.
id = 0  # Identifier for each file.
file = True  # Flag to toggle between adding file IDs and gaps.
for i in l:  # Iterate through the input list.
    if file:  # If `file` is True, add `i` instances of the current file ID to the disk.
        disk += [id] * i
        id += 1  # Increment the file ID for the next group of files.
    else:  # If `file` is False, add `i` gaps (represented by '.') to the disk.
        disk += ['.'] * i
    file = not file  # Toggle the `file` flag.

# Process the disk to remove gaps and adjust its contents.
pos = 0  # Initialize position pointer.
while pos < len(disk):  # Iterate through the disk until the end.
    if disk[pos] == '.':  # If the current position is a gap ('.'):
        disk[pos] = disk[-1]  # Replace it with the last element of the disk.
        disk = disk[:-1]  # Remove the last element (since it's now at `pos`).
        while disk[-1] == '.':  # If the new last element is a gap:
            disk = disk[:-1]  # Keep removing trailing gaps.
    pos += 1  # Move to the next position.

# Calculate the control checksum.
# The checksum is the sum of each position's value multiplied by its index.
checksum = sum([pos * disk[pos] for pos in range(len(disk))])

# Output the control checksum.
print(f'Control checksum is: {checksum}')