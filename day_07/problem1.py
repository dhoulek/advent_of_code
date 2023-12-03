import numpy as np

with open('input.txt', 'r') as f:
    input = [int(n) for n in f.readline().strip().split(',')]

num_crabs = len(input)
max_pos = max(input)

dist = [sum([abs(pos-input[crab]) for crab in range(num_crabs)]) 
        for pos in range(max_pos)]

cheapest = min(dist)
pos = dist.index(cheapest)

print(f'Cheapest alignment is at {pos} and costs {cheapest} fuels.')
