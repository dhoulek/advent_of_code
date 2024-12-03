# Advent of Code 2024, Day 3 Solution
# This script processes a text input to perform calculations based on specific patterns
# of multiplication instructions, both globally and within specific block conditions.

import re

# Read the entire input file as a single string.
with open('input.txt', 'r') as f:
    input = f.read()

# Define the regex pattern to identify multiplication instructions in the format "mul(x,y)".
# x and y are integers with 1 to 3 digits.
pattern = r"mul\(\d{1,3},\d{1,3}\)"

# Part 1: Calculate the sum of all multiplication instructions in the input.
matches = re.findall(pattern, input)  # Find all matches of the pattern in the input.

# Process each match to extract the numbers and compute their product.
result = 0
for instr in matches:
    numbers = instr[4:-1].split(',')  # Extract the numbers within "mul()".
    result += int(numbers[0]) * int(numbers[1])  # Multiply and add to the total.

# Output the total sum of all multiplication instructions.
print(f'Sum of the multiplication instructions is: {result}')

# Part 2: Process blocks of input within "do-don't" conditions.
# Split the input by the first occurrence of "don't()".
parts = input.split("don't()", maxsplit=1)
masked_inputs = parts[0]  # Initialize masked inputs with the part before the first "don't()".
on = False  # Track whether to include or skip the block.

# Iteratively process the input, alternating between including ("do()") and skipping ("don't()") blocks.
while len(parts) > 1:
    if on:
        # Include the current block and update parts to the next segment.
        parts = parts[1].split("don't()", maxsplit=1)
        masked_inputs += parts[0]
    else:
        # Skip the current block and update parts to the next segment.
        parts = parts[1].split("do()", maxsplit=1)
    on = not on  # Toggle the inclusion flag.

# Calculate the sum of multiplication instructions in the masked input.
matches = re.findall(pattern, masked_inputs)  # Find all matches in the masked input.

# Process each match to extract the numbers and compute their product.
result = 0
for instr in matches:
    numbers = instr[4:-1].split(',')
    result += int(numbers[0]) * int(numbers[1])

# Output the total sum of multiplication instructions within the "do-don't" blocks.
print(f'Sum of the multiplication instructions inside do-don\'t blocks is: {result}')