import numpy as np

# Open the input file and read the lines
# with open('test.txt', 'r') as f:  # Use this line for testing with a different file
with open('input.txt', 'r') as f:
    timeline = f.readline().strip().split(':')[-1]
    distline = f.readline().strip().split(':')[-1]

# Function to calculate winning options for each test case
def get_winning_options(time, dist):
    options = []
    for t, d in zip(time, dist):
        # Calculate the roots of the quadratic equation to find winning options
        r1 = (t - np.sqrt(t**2 - 4*d)) / 2    
        if r1 == np.ceil(r1):
            r1 = int(r1) + 1
        else:
            r1 = int(np.ceil(r1))
            
        r2 = (t + np.sqrt(t**2 - 4*d)) / 2
        if r2 == np.floor(r2):
            r2 = int(r2) - 1
        else:
            r2 = int(np.floor(r2))
        
        # Append the count of winning options for the current test case
        options.append(r2 - r1 + 1)
    return options

# Parse the input data into lists of integers
time = [int(i) for i in timeline.split(' ') if i != '']
dist = [int(i) for i in distline.split(' ') if i != '']

# Part 1: Calculate and print the product of ways to win for the given test cases
print('Part 1:')
print(f'Product of ways to win is {np.prod(get_winning_options(time, dist))}\n')

# Combine the time and dist lists into single integers for Part 2
time = int(timeline.replace(' ', ''))
dist = int(distline.replace(' ', ''))

# Part 2: Calculate and print the product of ways to win for a single test case
print('Part 2:')
print(f'Product of ways to win is {np.prod(get_winning_options([time], [dist]))}')