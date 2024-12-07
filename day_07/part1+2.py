# Advent of Code 2024, Day 7 Solution
# This script evaluates test cases to check if a target result can be generated
# from a list of numbers using specific operations for two problem parts.

from tqdm import tqdm  # For displaying progress in loops.
from math import log10, pow, ceil  # Math functions for calculations.

# Initialize counters to store the sum of valid results for both parts.
test_sum_part1 = 0  # Sum of results that satisfy Part 1 conditions.
test_sum_part2 = 0  # Sum of results that satisfy Part 2 conditions.

# Read the input file line by line.
with open('input.txt', 'r') as f:
    for l in tqdm(f.readlines()):  # Use tqdm to show progress.
        # Parse the result and the list of numbers from each line.
        result, numbers = l.strip().split(':')  # Split into result and numbers part.
        result = int(result)  # Convert the target result to an integer.
        numbers = [int(n) for n in numbers.split()]  # Convert the numbers into a list of integers.

        # Part 1: Initialize with the first number and calculate possible results.
        part1 = [numbers[0]]  # Start with the first number.
        part2 = [numbers[0]]  # Part 2 also starts with the first number.

        for n in numbers[1:]:  # Iterate through the rest of the numbers.
            # Part 1: Calculate new results by multiplying or adding the current number.
            old = part1.copy()  # Copy the current state of `part1`.
            part1 = [m * n for m in old] + [m + n for m in old]  # Generate new results.

            # Part 2: Includes an additional operation for generating results.
            old = part2.copy()  # Copy the current state of `part2`.
            # Generate results by multiplying, adding, or creating concatenated numbers.
            part2 = (
                [m * n for m in old] +  # Multiply.
                [m + n for m in old] +  # Add.
                [m * int(pow(10, ceil(log10(n + 1)))) + n for m in old]  # Concatenate.
            )

        # Check if the target result can be generated in Part 1.
        if result in part1:
            test_sum_part1 += result  # Add the result to the Part 1 sum if it matches.

        # Check if the target result can be generated in Part 2.
        if result in part2:
            test_sum_part2 += result  # Add the result to the Part 2 sum if it matches.

# Output the sums of valid results for both parts.
print(test_sum_part1)  # Total sum for Part 1.
print(test_sum_part2)  # Total sum for Part 2.
