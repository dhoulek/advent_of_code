# Part Two: Count every click where the dial points at 0 (method 0x434C49434B)

position = 50  # The dial starts pointing at 50
password = 0   # Counter for the number of times the dial points at 0

with open('input.txt') as f:
    for l in f.readlines():      # Read each rotation line
        if l[0] == 'L':          # Determine rotation direction
            f = -1               # Left rotation decreases position
        else:
            f = 1                # Right rotation increases position

        n = int(l.strip()[1:])   # Number of clicks to rotate

        # Rotate one click at a time
        for _ in range(n):
            position += f        # Move dial one step
            position %= 100      # Wrap around 0-99

            if position == 0:    # If the dial points at 0
                password += 1    # Increment the password counter

print(password)  # Print the final password
