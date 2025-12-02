# Read and preprocess the input
with open('input.txt') as f:
    # Read one line, strip newline, split by ',' → list of ranges as strings like "123-456"
    input = f.readline().strip().split(',')
    for i in range(len(input)):        
        # Split each "a-b" into ["a", "b"]
        input[i] = input[i].split('-')

invalid_ID = 0

# Iterate over each range pair
for r in input[:]:
    # Convert the two range endpoints to integers
    rint = [int(r[0]), int(r[1])]

    # l represents the length of the number we're constructing (digit count)
    # Only l between the digit-length of r[0] and r[1] are relevant
    for l in range(len(r[0]), len(r[1]) + 1):

        # Only consider even lengths because the constructed number repeats a half
        if l % 2 == 0:
            ll = l // 2  # Length of the repeated block

            # Determine minimum possible block value (bmin)
            if l == len(r[0]):
                # Match the prefix of the lower bound (ensures constructed number ≥ r[0])
                bmin = int(r[0][:ll])
            else:
                # If length is larger than lower bound's length, smallest ll-digit number
                bmin = int(10 ** (ll - 1))

            # Determine maximum possible block value (bmax)
            if l == len(r[1]):
                # Match prefix of upper bound (ensures constructed number ≤ r[1])
                bmax = int(r[1][:ll])
            else:
                # Largest ll-digit number
                bmax = int(10 ** ll - 1)

            # Loop over possible half-blocks
            for p in range(bmin, bmax + 1):
                # Construct the repeating number (e.g., p=12, ll=2 → "1212")
                n = int(f'{p}' * (l // ll))

                # Check if constructed number lies within the original range
                if rint[0] <= n <= rint[1]:
                    print(r, n)
                    invalid_ID += n

# Final result
print(f'Sum of invalid IDs: {invalid_ID}')