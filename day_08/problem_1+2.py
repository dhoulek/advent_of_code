from numpy import prod, lcm

# Read input file
with open('input.txt', 'r') as f:
    # Read the first line, representing the directions, and convert it to a list of integers
    directions = f.readline().strip().replace('L', '0').replace('R', '1')
    directions = [int(d) for d in directions]

    # Skip the second line in the file
    f.readline()

    # Create a dictionary to store node connections
    nodes = {}
    for l in f.readlines():
        # Parse each line to extract parent and child nodes
        p, nds = l.split('=')
        p = p.strip()
        l, r = nds.strip()[1:-1].split(',')
        l = l.strip()
        r = r.strip()
        nodes[p] = [l, r]

# Part 1: Traverse the nodes until reaching 'ZZZ'
print('Part 1:')
steps = 0
curr = 'AAA'
while curr != 'ZZZ':
    curr = nodes[curr][directions[steps % len(directions)]]
    steps += 1
print(f'Steps needed to reach ZZZ: {steps}\n')

# Part 2: Find the periodicity and calculate the steps needed for all nodes to end with 'Z'
# Manual analysis of the recursions shows that there are no crossings 
# of the node sequences, i.e. each starting node lead to only a single 
# type node ending with Z. I don't have any general proof for this, but 
# I am going to base my solution on the presumption that the above is 
# indeed true.
print('Part 2:')
steps = 0
last = 0
curr = [k for k in nodes.keys() if k[-1] == 'A']
init_phase = [0] * len(curr)
Znodes = [''] * len(curr)
periodicity = [0] * len(curr)

# Function to check if any node ends with 'Z'
def check(curr):
    return 'Z' in [n[-1] for n in curr]

while prod(periodicity) == 0:
    # Update current nodes based on directions
    curr = [nodes[c][directions[steps % len(directions)]] for c in curr]

    if check(curr):
        # Some node ends with Z
        for i in range(len(curr)):
            if curr[i][-1] == 'Z':
                if init_phase[i] == 0:
                    init_phase[i] = steps
                else:
                    if Znodes[i] == '':
                        Znodes[i] = curr[i]
                        periodicity[i] = steps - init_phase[i]
                    elif Znodes[i] != curr[i]:
                        # This should never happen, just for safety
                        print('ASSUMPTION DOES NOT HOLD')

    steps += 1

# Display the results for analysis
print(f' end nodes:     {Znodes}')
print(f' initial phase: {init_phase}')
print(f' periodicity:   {periodicity}')

# init_phase[i] = periodicity[i]-1!
# hence, we search for smallest integer N fulfilling 
#    N = init_phase[i] + n[i]*periodicity[i] 
#      = (n[i]+1)*periodicity[i] - 1
#    N' = n'[i]*periodicity[i]
# for every i. This means that N' is the least common multiple of
# {periodicity[i]}!

# Calculate the least common multiple (LCM) of periodicities
m = periodicity[0]
for i in range(1, len(periodicity)):
    m = lcm(m, periodicity[i])

print(f'Steps needed to nodes all ending with Z: {m}')