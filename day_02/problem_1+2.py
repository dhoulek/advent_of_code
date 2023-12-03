import numpy as np

# RGB mapping for numpy.array entries
mapping = dict(red=0, green=1, blue=2)


# Function to parse a line of input and extract game information
def parse_game(line):
    # Split the line into game identifier and sets information
    game, games = line.strip().split(':')
    
    # Extract the game ID from the game identifier
    gameid = int(game.strip().split()[-1])
    
    # Initialize an empty list to store sets information
    sets = []
    
    # Split the sets information and process each set
    for s in games.split(';'):
        # Split each set into individual cubes
        s = s.split(',')
        
        # Initialize an array to represent the RGB values for the set
        entry = np.zeros(3, dtype=np.int8)  # RGB
        
        # Process each cube in the set
        for e in s:
            # Split the cube into value and color
            e = e.split()
            
            # Update the corresponding RGB value in the entry array
            entry[mapping[e[1]]] = int(e[0])
        
        # Append the processed set to the list of sets
        sets.append(entry)
    
    # Return the extracted game ID and sets information
    return gameid, sets


# Constraint for the total number of cubes in the bag
bag_constraint = np.array([12, 13, 14])

# Lists to store results for problem 1 and problem 2
possible_gameids = []
powers = []

# Read input from a file ('input.txt') containing game information
# Change the file name to 'test.txt' if needed for testing
# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    # Iterate over each line of the input file
    for line in f.readlines():
        # Parse the game information from the current line
        gameid, sets = parse_game(line)
        
        # Problem 1: Check if the total number of cubes in each set is within the bag constraint
        possible = True
        for s in sets:
            if sum(s <= bag_constraint) < 3:
                possible = False
                break
        if possible:
            possible_gameids.append(gameid)
            
        # Problem 2: Calculate the product of the fewest cubes in each color for each game
        sets = np.array(sets).transpose()
        fewest_cubes = np.array([np.max(s) for s in sets])
        powers.append(np.prod(fewest_cubes))

# Print results for problem 1
print('Problem 1:')
print(f'Sum of possible game ids is: {sum(possible_gameids)}\n')

# Print results for problem 2
print('Problem 2:')
print(f'Sum of powers of minimum sets for each game is: {sum(powers)}')