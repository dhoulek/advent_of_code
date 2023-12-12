# Initialize an empty dictionary to store hands and their corresponding bids
bids = {}

# Read input file line by line and populate the bids dictionary
# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for l in f.readlines():
        h, b = l.strip().split()
        b = int(b)
        bids[h] = b

# Get a list of hands from the bids dictionary
hands = list(bids.keys())


# Function to determine the type of hand (e.g., one pair, three of a kind, etc.)
def get_type(a, joker=False):
    count = {}
    for c in list(a):
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1
    if len(count.keys()) == 1:
        return 7  # Five of a kind
    elif len(count.keys()) == 2:
        if joker and 'J' in count.keys():
            return 7  # Both four of a kind and full house can be five of a kind
        else:
            if sorted(count.values())[0] == 1:
                return 6  # Four of a kind
            else:
                return 5  # Full house
    elif len(count.keys()) == 3:
        if joker and 'J' in count.keys():
            if count['J'] == 1 and sorted(count.values())[-1] == 2:
                return 5  # One joker and two pair, make it a full house
            return 6  # Both three of a kind and two pair can be four of a kind
        else:
            if sorted(count.values())[-1] == 3:
                return 4  # Three of a kind
            else:
                return 3  # Two pair
    elif len(count.keys()) == 4:
        return 2  # One pair
    # High card
    return 1


# Function to compare two hands and determine if the first hand is stronger than the second
def is_stronger(a, b, joker=False):
    va = get_type(a, joker)
    vb = get_type(b, joker)
    if va > vb:
        return True
    elif va < vb:
        return False
    # Same type, compare individual cards
    for ca, cb in zip(list(a), list(b)):
        va = values.index(ca)
        vb = values.index(cb)
        if va > vb:
            return True
        elif va < vb:
            return False
    
    # Same hands (should not happen)
    print(f'I got twice the same hand: {a}, {b}')
    return None


# Function to perform a camel sort on a list of hands
def camel_sort(hands, joker=False):
    sorted_hand = False
    while not sorted_hand:
        sorted_hand = True
        for i in range(len(hands)-1):
            if is_stronger(hands[i], hands[i+1], joker):
                m = hands[i+1]
                hands[i+1] = hands[i]
                hands[i] = m
                sorted_hand = False
    return hands


# Part 1: Sort hands and calculate total winnings
print('Part 1:')
values = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))
hands = camel_sort(hands)
winnings = [(i+1)*bids[hands[i]] for i in range(len(hands))]
print(f'Total winnings are {sum(winnings)}\n')

# Part 2: Sort hands with joker and calculate total winnings
print('Part 2:')
values = list(reversed(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']))
hands = camel_sort(hands, joker=True)
winnings = [(i+1)*bids[hands[i]] for i in range(len(hands))]
print(f'Total winnings with JOKER are {sum(winnings)}')