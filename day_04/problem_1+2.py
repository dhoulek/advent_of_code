import pandas as pd
from tqdm import tqdm

# Dictionary to store input data for scratchcards
input_data = {}

# Read input from a file ('input.txt') containing scratchcard information
# Change the file name to 'test.txt' if needed for testing
with open('input.txt', 'r') as f:
    # Iterate over each line in the file
    for line in tqdm(f.readlines()):
        # Split the line into card number and scratchcard details
        card, numbers = line.split(':')
        
        # Extract the card number and convert it to an integer
        card = int(card.split(' ')[-1])
        
        # Split the scratchcard details into winning and played numbers
        winning, numbers = numbers.split('|')
        
        # Process function to convert space-separated numbers to a list of integers
        process = lambda l: [int(i) for i in l.strip().split() if i.isnumeric()]
        
        # Process winning and played numbers using the process function
        winning = process(winning)
        numbers = process(numbers)
        
        # Find matching numbers between played and winning numbers
        matching = [i for i in numbers if i in winning]
        
        # Calculate points based on the number of matching numbers
        points = 0
        if len(matching) > 0:
            points = 2 ** (len(matching) - 1)
        
        # Populate the input_data dictionary with card information
        input_data[card] = dict(
            winning=winning,
            numbers=numbers,
            matching=matching,
            points=points,
            multiplicity=1
        )

# Create a DataFrame from the input_data dictionary
input_df = pd.DataFrame(input_data).T

# Print results for Part 1
print('Part 1:')
print(f'Worth of the pile of the scratchcards: {input_df.points.sum()}')

# Loop to calculate the total number of scratchcards for Part 2
for i in tqdm(range(len(input_df))):
    for j in range(i + 1, min(len(input_df), i + 1 + len(input_df.iloc[i]['matching']))):
        input_df.iloc[j]['multiplicity'] += input_df.iloc[i]['multiplicity']

# Print results for Part 2
print('Part 2:')
print(f'Total number of the scratchcards: {input_df.multiplicity.sum()}')