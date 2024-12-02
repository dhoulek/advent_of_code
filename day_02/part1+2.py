# Advent of Code 2024, Day 2 Solution
# This script calculates the number of "safe" records and "safe with dumper" records
# based on specific conditions involving differences between consecutive values in a list.

import numpy as np

# Initialize counters for safe records and safe records with dumper.
safe = 0
safe_with_dumper = 0

# Open the input file and process it line by line.
with open('input.txt', 'r') as f:
    for l in f.readlines():
        # Read and parse each line into a NumPy array of integers.
        l = l.strip().split()
        l = np.array(l, dtype=np.int64)
        
        # Calculate the differences between consecutive elements in the list.
        diff = l[:-1] - l[1:]
        
        # Condition 1: Check if the differences are all positive or all negative.
        cond1 = np.logical_or(
            np.all(diff < 0),
            np.all(diff > 0)
        )
        
        # Condition 2: Check if the maximum absolute difference is between 1 and 3 (inclusive).
        cond2 = np.logical_and(
            1 <= np.max(np.abs(diff)),
            np.max(np.abs(diff)) <= 3
        )
        
        # Increment the safe counter if both conditions are met.
        safe += cond1 and cond2
        
        # Check for "safe with dumper" by removing one element at a time and re-evaluating conditions.
        for i in range(len(l)):
            # Create a new array by removing the i-th element.
            dump = np.delete(l, i)
            
            # Recalculate differences for the modified array.
            diff = dump[:-1] - dump[1:]
            
            # Re-check the conditions for the modified array.
            cond1 = np.logical_or(
                np.all(diff < 0),
                np.all(diff > 0)
            )
            cond2 = np.logical_and(
                1 <= np.max(np.abs(diff)),
                np.max(np.abs(diff)) <= 3
            )
            
            # If conditions are met, increment the safe_with_dumper counter and break.
            if cond1 and cond2:
                safe_with_dumper += 1
                break

# Print the results.
print(f'Number of safe records: {safe}')
print(f'Number of safe records with dumper: {safe_with_dumper}')