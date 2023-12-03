from itertools import product

def overlap(r1, r2):
    return (max(r1[0], r2[0]) <= min(r1[1], r2[1])) and \
        (max(r1[2], r2[2]) <= min(r1[3], r2[3])) and \
        (max(r1[4], r2[4]) <= min(r1[5], r2[5]))
    # return ((r1[1]>=r2[0]) or (r1[0]<=r2[1])) and \
    #     ((r1[3]>=r2[2]) or (r1[2]<=r2[3])) and \
    #     ((r1[5]>=r2[4]) or (r1[4]<=r2[5]))
        
def contained(r1, r2):
    return ((r1[0]>=r2[0]) and (r1[1]<=r2[1]) and\
        (r1[2]>=r2[2]) and (r1[3]<=r2[3]) and\
        (r1[4]>=r2[4]) and (r1[5]<=r2[5]))
    # or\
    #     ((r1[0]<=r2[0]) and (r1[1]>=r2[1]) and \
    #     (r1[2]<=r2[2]) and (r1[3]>=r2[3]) and \
    #     (r1[4]<=r2[4]) and (r1[5]>=r2[5]))        

def check_overlap(regions):
    for i1 in range(len(regions)-1):
        for i2 in range(i1+1, len(regions)):
            if overlap(regions[i1], regions[i2]):
                    return True, i1, i2
    return False, None, None

def chop_on(i1, i2, regions):
    r1 = regions[i1]
    r2 = regions[i2]
    if contained(r1, r2):
        new_regions = [r2]
    elif contained(r2, r1):
        new_regions = [r1]
    else:
        new_regions = []
        shift_min = [0,0,1]
        shift_max = [-1,0,0]
        x = sorted([r1[0], r1[1], r2[0], r2[1]])
        y = sorted([r1[2], r1[3], r2[2], r2[3]])
        z = sorted([r1[4], r1[5], r2[4], r2[5]])
        # print(x, y, z)
        if (len(x)<=2) and (len(y)<=2) and (len(z)<=2):
            new_regions = [r1]
        else:
            for ix, iy, iz in product(range(len(x)-1), range(len(y)-1), range(len(z)-1)):
                r = [x[ix]+shift_min[ix], x[ix+1]+shift_max[ix],
                    y[iy]+shift_min[iy], y[iy+1]+shift_max[iy],
                    z[iz]+shift_min[iz], z[iz+1]+shift_max[iz]]
                if contained(r, r1) or contained(r, r2):
                    # print('*', r, '*', r1, contained(r, r1), ';', r2, contained(r, r2))
                    # print('*', contained(r, r1), contained(r, r2))
                    new_regions.append(r)
    # print(len(regions))            
    regions = regions[:i2]+regions[i2+1:]
    regions = regions[:i1]+regions[i1+1:]
    # print(len(regions), len(new_regions))
    # print(r1, r2)
    # print(new_regions)
    regions += new_regions
    return regions

def chop_off(i1, off, regions):
    new_regions = []
    r1 = regions[i1]
    r2 = off
    if not contained(r1, off):
        shift_min = [0,0,1]
        shift_max = [-1,0,0]
        x = sorted([r1[0], r1[1], r2[0], r2[1]])
        y = sorted([r1[2], r1[3], r2[2], r2[3]])
        z = sorted([r1[4], r1[5], r2[4], r2[5]])
        # print(x, y, z)
        if (len(x)<=2) and (len(y)<=2) and (len(z)<=2):
            new_regions = []
        else:
            for ix, iy, iz in product(range(len(x)-1), range(len(y)-1), range(len(z)-1)):
                r = [x[ix]+shift_min[ix], x[ix+1]+shift_max[ix],
                    y[iy]+shift_min[iy], y[iy+1]+shift_max[iy],
                    z[iz]+shift_min[iz], z[iz+1]+shift_max[iz]]
                # print(r)
                if contained(r, r1) and not contained(r, r2):
                    # print('*', r, '*', r1, contained(r, r1), ';', r2, contained(r, r2))
                    # print('*', contained(r, r1), contained(r, r2))
                    # print(r)
                    new_regions.append(r)
    # print(len(regions))            
    regions = regions[:i1]+regions[i1+1:]
    # print(len(regions), len(new_regions))
    # print(r1, r2)
    # print(new_regions)
    regions += new_regions
    return regions
    
def process_line(line, regions):
    command, coords = line.split(' ')
    coords = [int(l.split('=')[-1]) for x in coords.split(',') for l in x.split('..')]
    if command == 'on':
        regions.append(coords)
        # print(regions)
        overlap, i1, i2 = check_overlap(regions)
        # print(overlap)
        while overlap:
            # print(regions)
            print(len(regions), i1, i2, regions[i1], regions[i2])
            regions = chop_on(i1, i2, regions)
            overlap, i1, i2 = check_overlap(regions)
    elif command == 'off':
        # print(command, coords)
        overlap, i1, _ = check_overlap(regions+[coords])
        while overlap:            
            print(overlap, i1, regions[i1])
            regions = chop_off(i1, coords, regions)            
            overlap, i1, _ = check_overlap(regions+[coords])
            # print(len(regions))
    # print(len(regions))
    return regions

def count_volume(regions):
    vol = 0
    for r in regions:
        v = (r[1]-r[0]+1)*(r[3]-r[2]+1)*(r[5]-r[4]+1)
        vol += v
    return vol

regions = []
with open('test2.txt', 'r') as f:
    for line in f:
        print(line.strip())
        regions = process_line(line.strip(), regions)
        print(f' actual number of "on" cubes: {count_volume(regions)}')
        print(f' number of regions: {len(regions)}\n')
print(f'final number of cubes in "on" state: {count_volume(regions)}')