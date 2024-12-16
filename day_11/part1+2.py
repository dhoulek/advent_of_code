# Advent of Code 2024 - Day 11, Combined Solution for Parts 1 and 2
# This script efficiently simulates the evolution of a collection of numbers ("stones")
# over multiple iterations ("blinks") using a dictionary for compact state representation.

# Read input data from the file 'input.txt'. Each number in the first line represents a stone.
with open('input.txt', 'r') as f:
    row = [int(s) for s in f.readline().strip().split()]

# Initialize a dictionary to count occurrences of each stone.
stones = dict()
for s in row:
    stones[s] = stones.get(s, 0) + 1

def blink(stones):
    """
    Processes stones stored as a dictionary of occurrences according to the rules:
    - If a stone's value is 0, it becomes 1.
    - If the number of digits in a stone is even, split the stone into two new stones.
    - If the number of digits in a stone is odd, multiply the stone by 2024.
    
    Args:
        stones (dict): Current stones, where keys are stone values and values are their counts.

    Returns:
        dict: Updated stones after one "blink."
    """
    new = dict()
    for s in stones.keys():
        count = stones[s]  # Number of occurrences of the stone.
        st = str(s)  # Convert the stone value to a string to analyze its digits.
        l = len(st)  # Length of the string representation (number of digits).
        
        if s == 0:
            # Rule: If stone is 0, it becomes 1.
            new[1] = new.get(1, 0) + count
        elif l % 2 == 0:
            # Rule: If the number of digits is even, split the stone.
            for n in [int(st[:l//2]), int(st[l//2:])]:
                new[n] = new.get(n, 0) + count
        else:
            # Rule: If the number of digits is odd, multiply the stone by 2024.
            new[s * 2024] = new.get(s * 2024, 0) + count
    return new

# Simulate 75 "blinks" and print results for Part 1 (after 25 blinks) and Part 2 (after 75 blinks).
for i in range(75):
    stones = blink(stones)
    if i in [24, 74]:
        # Sum the counts of all stones to get the total number of stones.
        print(f'Number of stones after {i+1} blinks: {sum(stones.values())}')