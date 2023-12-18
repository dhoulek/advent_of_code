import numpy as np

# Function to find the horizontal mirror in a matrix
def find_horizontal_mirror(A, smudge):
    n, _ = A.shape
    for y in range(1, n):
        Y = min(y, n-y)
        # Extract upper and lower parts for mirroring
        A1 = A[max(0, y-Y): y, :]
        A2 = A[min(n, y+Y-1): y-1: -1, :]
        # Calculate the sum of absolute differences between the mirrored parts
        if np.sum(np.abs(A1 - A2)) == smudge:
            return y
    return None

# Function to find the mirror, either horizontally or vertically
def find_mirror(A, smudge):
    hm = find_horizontal_mirror(A, smudge)
    if hm is not None:
        return hm * 100
    else:
        # Transpose the matrix to find vertical mirror
        vm = find_horizontal_mirror(A.T, smudge)
        return vm

# Initialize counters for notes
notes = 0
notes_smudge = 0

# Read input from a file
with open('input.txt', 'r') as f:
    A = []    
    for l in f.readlines():
        l = l.strip()
        if l == '':
            # Update notes counters for each block in the input
            notes += find_mirror(np.array(A), 0)
            notes_smudge += find_mirror(np.array(A), 1)
            A = []  # Reset the matrix for the next block
        else:
            # Convert each line into a binary array and add it to the matrix
            A.append(np.array([1 if c == '#' else 0 for c in l]))

    # Process the last block in case the input does not end with an empty line
    notes += find_mirror(np.array(A), 0)
    notes_smudge += find_mirror(np.array(A), 1)

# Print results for both parts
print('Part 1:')
print(f'Sum of notes {notes}\n')

print('Part 2:')
print(f'Sum of notes with smudge {notes_smudge}\n')