# Advent of Code 2024 - Day 11, Part 1
# This script processes a list of numbers ("stones") iteratively according to specific rules,
# simulating 25 "blinks." After the simulation, it prints the number of stones remaining.

# Read input data from the file 'input.txt'. Each number in the first line represents a stone.
with open('input.txt', 'r') as f:
    stones = [int(s) for s in f.readline().strip().split()]

def blink(stones):
    """
    Processes a list of stones according to the following rules:
    - If a stone's value is 0, it becomes 1.
    - If the number of digits in a stone is even, split the stone into two new stones:
      one formed by the first half of its digits, and the other by the second half.
    - If the number of digits in a stone is odd, multiply the stone by 2024.
    
    Args:
        stones (list of int): The current list of stones.

    Returns:
        list of int: The updated list of stones after one "blink."
    """
    new = []
    for s in stones:
        st = str(s)  # Convert the stone value to a string to analyze its digits.
        l = len(st)  # Length of the string representation (number of digits).
        
        if s == 0:
            new.append(1)  # Rule: If stone is 0, it becomes 1.
        elif l % 2 == 0:
            # Rule: If the number of digits is even, split the stone.
            new.append(int(st[:l//2]))  # First half of the digits.
            new.append(int(st[l//2:]))  # Second half of the digits.
        else:
            # Rule: If the number of digits is odd, multiply the stone by 2024.
            new.append(s * 2024)
    return new

# Simulate 25 "blinks" by repeatedly applying the "blink" function.
for i in range(25):
    stones = blink(stones)

# Output the total number of stones after 25 blinks.
print(f'Number of stones after {i+1} blinks: {len(stones)}')