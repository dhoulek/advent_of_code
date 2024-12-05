# A small routine to understand the input structure for Day 5
# This script reads a test input file, separates rules and orders,
# and checks if the sets of numbers in both sections match.

# Open and read the input file.
with open('test.txt', 'r') as f:
    rules = []  # To store numbers from the rules section.
    orders = []  # To store numbers from the orders section.
    first_section = True  # Tracks whether we are in the rules section of the input.

    # Process each line of the input.
    for l in f.readlines():
        if len(l.strip()) == 0:  # An empty line separates rules from orders.
            first_section = False
        else:
            if first_section:
                # Parse numbers from the rules section (separated by "|").
                rules += [int(i) for i in l.strip().split('|')]
            else:
                # Parse numbers from the orders section (separated by ",").
                orders += [int(i) for i in l.strip().split(',')]

# Convert rules and orders to sets to deduplicate numbers.
rules = set(rules)
orders = set(orders)

# Print the unique numbers found in each section.
print(f'Numbers in rules: {rules}')
print(f'Numbers in orders: {orders}')

# Check if the sets of numbers in rules and orders are identical.
if rules == orders:
    print('Both are the same!')
else:
    print('O-o! Problem!')