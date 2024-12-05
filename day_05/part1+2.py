# Advent of Code 2024, Day 5 Solution
# This script processes a set of rules and orders to validate and sort them based on the rules.
# It calculates sums of middle elements from correctly and incorrectly sorted lists.

# Read and parse the input file.
with open('input.txt', 'r') as f:
    rules = []  # To store the rule pairs.
    numbers = []  # To store all unique numbers mentioned in the rules.
    orders = []  # To store the orders to be validated and sorted.
    first_section = True  # Tracks whether we are in the rules section of the input.

    for l in f.readlines():
        if len(l.strip()) == 0:  # Empty line separates rules from orders.
            first_section = False
        else:
            if first_section:
                # Parse rules as pairs of integers separated by "|".
                rules.append([int(i) for i in l.strip().split('|')])
                numbers += [int(i) for i in l.strip().split('|')]
            else:
                # Parse orders as lists of integers separated by ",".
                orders.append([int(i) for i in l.strip().split(',')])

# Deduplicate numbers to get a list of unique values.
numbers = list(set(numbers))

# Function to check if a given pair of numbers satisfies the rules.
def check_rules(a, b):
    return [a, b] in rules

# Function to sort an order based on the rules.
def sort_order(order):
    order = order.copy()  # Create a copy to avoid modifying the original list.
    passed = False  # Tracks if the list is fully sorted.
    while not passed:
        passed = True
        for i in range(len(order) - 1):
            # Compare each adjacent pair in the list.
            a, b = order[i: i+2]
            if not check_rules(a, b):  # If the pair doesn't follow the rules, swap them.
                order[i] = b
                order[i+1] = a
                passed = False  # Continue the loop as the list may still be unsorted.
    return order

# Analyze the orders.
middle = []  # To store the middle elements of correctly sorted lists.
middle_incorrectly = []  # To store the middle elements of incorrectly sorted lists.

for order in orders:
    if order == sort_order(order):  # Check if the order is already sorted correctly.
        middle.append(order[len(order) // 2])  # Add the middle element to the correct list.
    else:
        # Add the middle element of the corrected (sorted) list to the incorrect list.
        middle_incorrectly.append(sort_order(order)[len(order) // 2])

# Calculate and print the results.
print(f'Sum of middle pages from correctly ordered lists: {sum(middle)}')
print(f'Sum of middle pages from incorrectly ordered lists: {sum(middle_incorrectly)}')