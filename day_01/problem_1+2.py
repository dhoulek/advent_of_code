def replace_words(line):
    nums = dict(one='o1e', two='t2o', three='t3e', four='f4r', 
                five='f5e', six='s6x', seven='s7n', eight='e8t', 
                nine='n9e')
    for k in nums.keys():
        line = line.replace(k, str(nums[k]))
    return line

def find_calibration_value(line):
    # get list of characters
    line = list(line.strip())
    # search for first digit
    l = list(reversed(line.copy()))
    first = l.pop()
    while not str.isnumeric(first):
        first = l.pop()
    # search for the last digit
    l = line.copy()
    last = l.pop()
    while not str.isnumeric(last):
        last = l.pop()
    # return the number
    return int(first+last)

numbers = []
numbers2 = []

with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
# with open('test2.txt', 'r') as f:
    for line in f.readlines():
        numbers.append(find_calibration_value(line))
        numbers2.append(find_calibration_value(replace_words(line)))
# print(numbers2)

# problem 1
print('Part 1:')
print(f'Sum of all decoded calibration values is: {sum(numbers)}\n')

# problem 2
print('Part 2:')
print(f'Sum of all decoded calibration values is: {sum(numbers2)}\n')