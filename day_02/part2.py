# Read and preprocess the input
with open('input.txt') as f:
    # Read the line, split at commas (producing items like "100-999")
    input = f.readline().strip().split(',')
    for i in range(len(input)):        
        # Split each range "a-b" into ["a", "b"]
        input[i] = input[i].split('-')

invalid_ID = []  # Collect all invalid IDs (duplicates removed later)

# Process each range r = ["a", "b"]
for r in input[:]:
    # Convert bounds to integers
    rint = [int(r[0]), int(r[1])]

    aux = []  # Temporary list of all invalid numbers found for this range

    # Loop over all possible lengths l of candidate numbers
    for l in range(len(r[0]), len(r[1]) + 1):

        # For this part, we try any block size ll such that:
        #   - 1 ≤ ll ≤ l/2
        #   - l is divisible by ll
        # So numbers can be made of repeated blocks of ANY size, not just half
        for ll in [i for i in range(1, l // 2 + 1) if l % i == 0]:

            # Compute smallest possible starting block (bmin)
            if l == len(r[0]):
                # Same-length numbers must match the lower bound prefix
                bmin = int(r[0][:ll])
            else:
                # Otherwise smallest ll-digit number
                bmin = int(10 ** (ll - 1))

            # Compute largest possible starting block (bmax)
            if l == len(r[1]):
                # Match upper bound prefix for same-length numbers
                bmax = int(r[1][:ll])
            else:
                # Otherwise largest ll-digit number
                bmax = int(10 ** ll - 1)

            # Try all possible block values p
            for p in range(bmin, bmax + 1):
                # Build the repeated-pattern candidate number
                # Example: p=12, ll=2, l=6 → "121212"
                n = int(f'{p}' * (l // ll))

                # Check if n lies within the original range
                if rint[0] <= n <= rint[1]:
                    aux.append(n)

    # Convert to set to remove duplicates
    print(r, set(aux))

    # Add unique found values to global list
    invalid_ID += list(set(aux))

# Print final sum
print(f'Sum of invalid IDs: {sum(invalid_ID)}')