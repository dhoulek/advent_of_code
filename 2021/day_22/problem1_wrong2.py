from itertools import product
from os import remove

def overlap(r1, r2):
    return (max(r1[0], r2[0]) <= min(r1[1], r2[1])) and \
        (max(r1[2], r2[2]) <= min(r1[3], r2[3])) and \
        (max(r1[4], r2[4]) <= min(r1[5], r2[5]))
        
def contained(r1, r2):
    return ((r1[0]>=r2[0]) and (r1[1]<=r2[1]) and\
        (r1[2]>=r2[2]) and (r1[3]<=r2[3]) and\
        (r1[4]>=r2[4]) and (r1[5]<=r2[5]))  

def check_overlap(regions):
    for i1 in range(len(regions)-1):
        for i2 in range(i1+1, len(regions)):
            if overlap(regions[i1], regions[i2]):
                    return True, i1, i2
    return False, None, None

def get_limits(l):
    l = sorted(l)
    s = set(l)
    if len(s) == 1:
        lower = [l[0]]
        upper = [l[0]]
    elif len(s) == 2:
        if l[1] != l[2]:
            lower = [l[0]]
            upper = [l[2]]
        else:
            if l[0]==l[1]:
                lower = [l[0], l[0]+1]
                upper = [l[0], l[2]]
            else:
                lower = [l[0], l[1]]
                upper = [l[1]-1, l[1]]
    elif len(s) == 3:
        if l[0]==l[1]:
            lower = [l[0], l[2]+1]
            upper = [l[2], l[3]]
        elif l[1]==l[2]:
            lower = [l[0], l[1], l[2]+1]
            upper = [l[1]-1, l[2], l[3]]
        else:
            lower = [l[0], l[1]]
            upper = [l[1]-1, l[2]]
    else:
        lower = [l[0], l[1], l[2]+1]
        upper = [l[1]-1, l[2], l[3]]
    return lower, upper

def chop_on(i1, i2, add_regions, remove_regions):
    r1 = add_regions[i1]
    r2 = add_regions[i2]
    add = []
    remove = []
    if contained(r1, r2):
        remove += [r1]
    elif contained(r2, r1):
        remove += [r2]
    else:
        x_low, x_up = get_limits([r1[0], r1[1], r2[0], r2[1]])
        y_low, y_up = get_limits([r1[2], r1[3], r2[2], r2[3]])
        z_low, z_up = get_limits([r1[4], r1[5], r2[4], r2[5]])
        for ix, iy, iz in product(range(len(x_low)), range(len(y_low)), range(len(z_low))):
            r = [x_low[ix], x_up[ix], y_low[iy], y_up[iy], z_low[iz], z_up[iz]]
            if contained(r, r1) and contained(r, r2):
                # print('*', r, '*', r1, contained(r, r1), ';', r2, contained(r, r2))
                remove.append(r)
    return add, remove

def chop_off(i1, off, add_regions, remove_regions):
    r1 = add_regions[i1]
    r2 = off
    add = []
    remove = []
    if contained(r1, off):
        remove.append(r2)
    else:
        x_low, x_up = get_limits([r1[0], r1[1], r2[0], r2[1]])
        y_low, y_up = get_limits([r1[2], r1[3], r2[2], r2[3]])
        z_low, z_up = get_limits([r1[4], r1[5], r2[4], r2[5]])
        for ix, iy, iz in product(range(len(x_low)), range(len(y_low)), range(len(z_low))):
            r = [x_low[ix], x_up[ix], y_low[iy], y_up[iy], z_low[iz], z_up[iz]]
            # print(r)
            if contained(r, r1) and contained(r, r2):
                # print('*', r, '*', r1, contained(r, r1), ';', r2, contained(r, r2))
                # print('*', contained(r, r1), contained(r, r2))
                # print(r)
                remove.append(r)
    # print(len(regions))            
    # regions = regions[:i1]+regions[i1+1:]
    # # print(len(regions), len(new_regions))
    # # print(r1, r2)
    # # print(new_regions)
    # regions += new_regions
    return add, remove
    
def process_line(line, add_regions, remove_regions):
    command, coords = line.split(' ')
    coords = [int(l.split('=')[-1]) for x in coords.split(',') for l in x.split('..')]
    if command == 'on':
        add_regions.append(coords)
        i2 = len(add_regions)-1
        add = []
        remove = []
        for i1 in range(len(add_regions)-1):
            if overlap(add_regions[i1], add_regions[i2]):
                # print(len(add_regions), i1, i2, add_regions[i1], add_regions[i2])
                _, r = chop_on(i1, i2, add_regions, remove_regions)
                if len(r)>1:
                    print('CONFUSION!!!!')
                remove += r
                # print('removing', r)
        for i1 in range(len(remove_regions)):
            for i2 in range(len(remove)):
                if overlap(remove_regions[i1], remove[i2]):
                    _, r = chop_off(i1, remove[i2], remove_regions, [])
                    # print('adding', r)
                    add += r
                # print(len(add), len(remove))
                # add_regions += add
            # overlap, i1, i2 = check_overlap(regions)
    elif command == 'off':
        # print(command, coords)
        # overlap, i1, _ = check_overlap(regions+[coords])
        add = []
        remove = []
        for i1 in range(len(add_regions)):
            if overlap(add_regions[i1], coords):
                _, r = chop_off(i1, coords, add_regions, remove_regions)        
                if len(r)>1:
                    print('CONFUSION!!!!')
                remove += r
        # print('---', remove)
        for i1 in range(len(remove)-1):
            for i2 in range(i1+1, len(remove)):
                if overlap(remove[i1], remove[i2]):
                    _, r = chop_on(i1, i2, remove, [])
                    # print('adding', r)
                    add += r
    add_regions += add
    remove_regions += remove
        #     print(overlap, i1, regions[i1])
        #     regions = chop_off(i1, coords, regions)            
        #     overlap, i1, _ = check_overlap(regions+[coords])
            # print(len(regions))
    # print(len(regions))
    return add_regions, remove_regions

def count_volume(add_regions, remove_regions):
    vol = 0
    for r in add_regions:
        v = (r[1]-r[0]+1)*(r[3]-r[2]+1)*(r[5]-r[4]+1)
        vol += v
    for r in remove_regions:
        v = (r[1]-r[0]+1)*(r[3]-r[2]+1)*(r[5]-r[4]+1)
        vol -= v
    return vol

add_regions = []
remove_regions = []
with open('test1.txt', 'r') as f:
    for line in f:
        print(line.strip())
        add_regions, remove_regions = process_line(line.strip(), add_regions, remove_regions)
        # print(' +: ', add_regions)
        # print(' -: ', remove_regions)
        print(f' actual number of "on" cubes: {count_volume(add_regions, remove_regions)}')
        # print(f' number of regions: {len(regions)}\n')
# print(f'final number of cubes in "on" state: {count_volume(regions)}')

