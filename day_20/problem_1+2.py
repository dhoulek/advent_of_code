from tqdm import tqdm

with open('input.txt', 'r') as f:
    orig_data = [int(x.strip()) for x in f.readlines()]

def move(pos):
    global order
    global data
    index = order.index(pos)
    change = data[index]
    # the number of spaces when circling the list is len(data)-1
    new_index = (index+change) % (len(data)-1)
    if new_index == 0:
        new_index = len(data)
    
    data.pop(index)
    data.insert(new_index, change)
    order.pop(index)
    order.insert(new_index, pos)
    
def get(pos):
    index = data.index(0)
    return data[(index+pos) % len(data)]


print('---------- PART 1 -----------')
print()
key = int(1)
repetitions = 1
data = [i*key for i in orig_data]
# initial order of the data
order = list(range(len(data)))

for _ in tqdm(range(repetitions)):
    for i in range(len(data)):
        move(i)
        
print()    
print(f'final coordinate is: {get(1000)+get(2000)+get(3000)}')
print()

print('---------- PART 2 -----------')
print()
key = int(811589153)
repetitions = 10
data = [i*key for i in orig_data]
# initial order of the data
order = list(range(len(data)))

for _ in tqdm(range(repetitions)):
    for i in range(len(data)):
        move(i)
print()    
print(f'final coordinate is: {get(1000)+get(2000)+get(3000)}')
