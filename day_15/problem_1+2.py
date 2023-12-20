# Function to calculate hash value based on the given rules
def calculate_hash_value(s, label=False):
    v = 0
    for c in s:
        # Break the loop if label is True and the character is '=' or '-'
        if label and c in ['=', '-']:
            break
        v = (v + ord(c)) * 17 % 256
    return v

# Read input from 'input.txt' file
with open('input.txt', 'r') as f:
    # Split the comma-separated values into a list
    lines = f.readline().strip().split(',')

# Calculate hash values for each input string
hash_values = [calculate_hash_value(s) for s in lines]
print('Part 1:')
print(f'Sum of the hashes is {sum(hash_values)}\n')

# Initialize boxes with label and focus lists
boxes = [{'label': [], 'focus': []} for _ in range(256)]

# Process each input string to update lens configurations
for s in lines:
    h = calculate_hash_value(s, label=True)
    
    if s[-1] == '-':
        # Remove lens if the label exists in the box
        label = s[:-1]
        if label in boxes[h]['label']:
            i = boxes[h]['label'].index(label)
            boxes[h]['label'].pop(i)
            boxes[h]['focus'].pop(i)
    else:
        # Add or replace lens with the given label and focus
        label, focus = s.split('=')
        focus = int(focus)
        if label in boxes[h]['label']:
            # Replace lens if the label already exists in the box
            i = boxes[h]['label'].index(label)
            boxes[h]['focus'][i] = focus
        else:
            # Add new lens if the label doesn't exist in the box
            boxes[h]['label'].append(label)
            boxes[h]['focus'].append(focus)

# Calculate the focusing power for Part 2
focus_power = 0
for i, b in enumerate(boxes):
    for j, f in enumerate(b['focus']):
        focus_power += (i + 1) * (j + 1) * f

# Print the result for Part 2
print('Part 2:')
print(f'The focusing power of the resulting lens configuration is {focus_power}')