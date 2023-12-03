from tqdm import tqdm

img = {}
with open('input.txt', 'r') as f:
    algo = {bin(i)[2:].zfill(9): 0 if c=='.' else 1 for i, c in enumerate(f.readline().strip())}
    # algo = {bin(i)[2:].zfill(9): 1 if c=='.' else 0 for i, c in enumerate(f.readline().strip())}
    f.readline()
    y = 0
    for line in f.readlines():
        img[y] = [x for x,c in enumerate(line.strip()) if c=='#']
        y += 1

def get_size(img):
    maxx = max(img[list(img.keys())[0]])
    minx = min(img[list(img.keys())[0]])
    for row in img.values():
        maxx = max(maxx, max(row))
        minx = min(minx, min(row))
    maxy = max(img.keys())
    miny = min(img.keys())
    return miny, maxy, minx, maxx

def get_value(img, x, y):
    try:
        res = x in img[y]
    except:
        return 0
    else:
        return int(res)

def apply_algo(img, state):
    new = {}
    miny, maxy, minx, maxx = get_size(img)
    for y in range(miny-3, maxy+3):
        row = []
        for x in range(minx-2, maxx+3):
            s = ''
            for iy in range(y-1, y+2):
                for ix in range(x-1, x+2):
                    if iy<miny or iy>maxy or ix<minx or ix>maxx:
                        s += str(state)
                    else:
                        s += str(get_value(img, ix, iy))
            if algo[s]==1:
                row.append(x)
        if len(row)>0:
            new[y] = row
    if algo['000000000'] == 1:
        if state == 1:
            state = 0
        else:
            state = 1
    return new, state

def count_pixels(img):
    return sum([len(row) for row in img.values()])

state = 0
print(f'initial image size: {get_size(img)}')

for _ in tqdm(range(2)):
    img, state = apply_algo(img, state)
print(f'image size after 2 enhancements: {get_size(img)}')
print(f'number of lit up pixel after 2 enhancements: {count_pixels(img)}')

for _ in tqdm(range(48)):
    img, state = apply_algo(img, state)
print(f'image size after 50 enhancements: {get_size(img)}')
print(f'number of lit up pixel after 50 enhancements: {count_pixels(img)}')
