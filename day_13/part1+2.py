# Advent of Code 2024 - Day 13, Solution for Both Parts
# This script computes two results by processing coordinate systems and solving linear equations.
# Part 1: Misaligned adjustment is not applied.
# Part 2: Misaligned adjustment of +10 trillion is applied.

import re
import numpy as np

def solve(M, misaligned=False):
    """
    Solves for A and B given a system of equations represented by matrix M and vector b.

    Args:
        M (list of lists): The coefficient matrix and the vector b (last row of M).
        misaligned (bool): If True, adds 10 trillion to vector b.

    Returns:
        tuple: (A, B) if the solution is valid, or (0, 0) if not.
    """
    b = np.array(M.pop())  # Extract the last row as vector b.
    if misaligned:
        b += 10000000000000  # Apply misaligned adjustment if required.
    M = np.array(M).T  # Transpose the remaining matrix to form the coefficient matrix.

    # Compute A and its remainder.
    divident = b[0] * M[1, 1] - b[1] * M[0, 1]
    divisor = M[0, 0] * M[1, 1] - M[1, 0] * M[0, 1]
    sgn = np.sign(divisor)
    divident *= sgn
    divisor *= sgn
    A = divident // divisor
    Arest = divident % divisor

    # Compute B and its remainder.
    divident = b[0] * M[1, 0] - b[1] * M[0, 0]
    divisor = M[1, 0] * M[0, 1] - M[0, 0] * M[1, 1]
    sgn = np.sign(divisor)
    divident *= sgn
    divisor *= sgn
    B = divident // divisor
    Brest = divident % divisor

    # Return the solution only if both remainders are zero.
    if Arest == 0 and Brest == 0:
        return A, B
    return 0, 0

M = []  # List to store the matrix of coefficients and vector b.
price = 0  # Result for Part 1.
price_part2 = 0  # Result for Part 2.

# Read input data from 'input.txt'.
with open('input.txt', 'r') as f:
    for l in f.readlines() + [" "]:
        match = re.match(r".*X.(?P<X>\d*), Y.(?P<Y>\d*)", l)
        if match:
            # Append coordinates to matrix M.
            M.append([int(x) for x in match.groups()])
        else:
            # Solve for Part 1 (without misalignment).
            A, B = solve(M.copy(), misaligned=False)
            price += 3 * A + B

            # Solve for Part 2 (with misalignment).
            A, B = solve(M.copy(), misaligned=True)
            price_part2 += 3 * A + B

            # Reset matrix M for the next group.
            M = []

# Output the results for both parts.
print('Number of tokens in part 1:', price)
print('Number of tokens in part 2:', price_part2)