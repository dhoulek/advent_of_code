numbers = []
with open('1.in', 'r') as input:
    for line in input.readlines():
        numbers.append(int(line.split()[0]))
print(numbers)

for i in numbers:
    for j in numbers:
        if i+j==2020:
            print (i, j, i+j, i*j)
            
for i in numbers:
    for j in numbers:
        for k in numbers:
            if i+j+k==2020:
                print (i, j, k, i+j+k, i*j*k)