# Function to replace words in a line with their corresponding numeric representations
def replace_words(line):
    # Dictionary mapping words to their numeric representations
    # we keep the first and last letter to correctly decode 
    # e.g. 'oneight' into '18'
    nums = dict(one='o1e', two='t2o', three='t3e', four='f4r', 
                five='f5e', six='s6x', seven='s7n', eight='e8t', 
                nine='n9e')
    
    # Replace words in the line with their numeric representations
    for k in nums.keys():
        line = line.replace(k, str(nums[k]))
    return line


# Function to find the calibration value from a line
def find_calibration_value(line):
    # Convert the line into a list of characters
    line = list(line.strip())
    
    # Search for the first digit from the end of the line
    l = list(reversed(line.copy()))
    first = l.pop()
    while not str.isnumeric(first):
        first = l.pop()
    
    # Search for the last digit
    l = line.copy()
    last = l.pop()
    while not str.isnumeric(last):
        last = l.pop()
    
    # Return the numeric value formed by concatenating the first and last digits
    return int(first + last)


# Lists to store calibration values for problem 1 and problem 2
numbers = []
numbers2 = []

# Read input from a file ('input.txt') containing lines with words to be replaced
# Change the file name to 'test.txt' or 'test2.txt' if needed for testing
with open('input.txt', 'r') as f:
    # Iterate over each line in the file
    for line in f.readlines():
        # Find and store the calibration value for the original line
        numbers.append(find_calibration_value(line))
        
        # Find and store the calibration value for the line with replaced words
        numbers2.append(find_calibration_value(replace_words(line)))

# Print results for problem 1
print('Part 1:')
print(f'Sum of all decoded calibration values is: {sum(numbers)}\n')

# Print results for problem 2
print('Part 2:')
print(f'Sum of all decoded calibration values with replaced words is: {sum(numbers2)}')