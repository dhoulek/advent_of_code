import numpy as np
from itertools import product

scanners = []
with open('input.txt', 'r') as f:
    for line in f.readlines():        
        if line.strip()[:3] == '---':
            # staring new scanner
            beacon_list = []
        elif len(line.strip()) == 0:
            scanners.append(beacon_list)
        else:            
            beacon_list.append(np.array([int(x) for x in line.strip().split(',')]))
scanners.append(beacon_list)

print(f' in total read {len(scanners)} scanners')
print(f' numbers of beacons each scanner sees: {[len(l) for l in scanners]}')

def check_overlap(alpha, beta):
    # alpha, beta: indices of scanners
    beacons_alpha = scanners[alpha]
    beacons_beta = scanners[beta]
    sgn = list(np.array(s) for s in product([-1,1], [-1,1], [-1,1]))
    ax_rot = [[0,1,2], [1,2,0], [2,0,1], [0,2,1], [1,0,2], [2,1,0]]
    found = False
    for s in sgn:
        for r in ax_rot:
            diff = {}
            list_alpha = {}
            list_beta = {}
            for vi, v in enumerate(beacons_alpha):
                for wi, w in enumerate(beacons_beta):
                    wprime = w*s
                    d = v - np.array([wprime[r[i]] for i in range(3)])
                    k = ','.join((d).astype(str))
                    if k in diff.keys():
                        diff[k] += 1
                        list_alpha[k].append(vi)
                        list_beta[k].append(wi)
                    else:
                        diff[k] = 1
                        list_alpha[k] = [vi]
                        list_beta[k] = [wi]
            if max(diff.values()) >= 12:
                found = True
                break
        if found:
            break
    i = list(diff.keys())[list(diff.values()).index(max(diff.values()))]
    return found, list_alpha[i], list_beta[i], s, r


# performing analysis of scanner position
todo = list(range(1, len(scanners)))
analyze = [0]
rot = [[0,1,2]] + [None for i in range(len(scanners)-1)]
sgn = [np.array([1,1,1])] + [None for i in range(len(scanners)-1)]
diff = [np.array([0,0,0])] + [None for i in range(len(scanners)-1)]
while len(todo)>0:
    alpha = analyze[0]
    analyze = analyze[1:]
    print(f'analyzing {alpha}, todo: {todo}')
    for ibeta in reversed(range(len(todo))):
        beta = todo[ibeta]
        overlap, list_alpha, list_beta, s, r = check_overlap(alpha, beta)
        if overlap:
            todo = todo[:ibeta]+todo[ibeta+1:]
            analyze.append(beta)
            rot[beta] = [r[rot[alpha][i]] for i in range(3)]
            sgn[beta] = sgn[alpha]*[s[rot[beta][i]] for i in range(3)]
            v = [scanners[alpha][list_alpha[0]][rot[alpha][i]] for i in range(3)]*sgn[alpha]
            w = [scanners[beta][list_beta[0]][rot[beta][i]] for i in range(3)]*sgn[beta]
            d = v-w
            diff[beta] = diff[alpha]+d
            

# problem 1
# number of unique beacons
beacons = [','.join([str(x) for x in beacon]) for beacon in scanners[0]]
for s in range(1, len(scanners)):
    for b in scanners[s]:
        w = np.array([b[rot[s][i]] for i in range(3)])*sgn[s]+diff[s]
        beacons.append(','.join([str(x) for x in w]))
print(f'there are {len(set(beacons))} unique beacons')


# problem 2
dist = 0
for i in range(len(scanners)-1):
    for j in range(i+1, len(scanners)):
        dist = max(dist, sum([abs(diff[i][k]-diff[j][k]) for k in range(3)]))
print(f'maximum distance is {dist}')
