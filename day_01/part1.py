# Initialize the starting position of the dial and the password counter
position = 50      # The dial starts pointing at 50
password = 0       # Counts how many times the dial points at 0

# Open the input file containing the sequence of rotations
with open('input.txt') as f:
    for l in f.readlines():  # Read the file line by line
        # Determine the direction of rotation
        if l[0] == 'L':       # If the line starts with 'L', turn left
            f = -1            # Left rotation decreases the position
        else:                 # Otherwise, it's a right rotation
            f = 1             # Right rotation increases the position

        # Extract the number of steps (distance) to rotate
        n = int(l.strip()[1:])  # Remove any whitespace and convert to int

        # Apply the rotation to the current position
        position += f * n       # Move the dial left or right by n steps

        # Check if the dial is pointing at 0 (modulo 100 because it's circular)
        if position % 100 == 0:  # Dial has 100 positions (0-99)
            password += 1        # Increment the counter if it's at 0

# Print the final password (number of times the dial points at 0)
print(password)
