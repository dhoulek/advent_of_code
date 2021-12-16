with open('input.txt', 'r') as f:
    input = f.readline().strip()
    
#convert hex to bin
len_hex = len(input)
input = bin(int(input, 16))[2:].zfill(len_hex*4)
# print(input, len(input), len_hex)

def parse_number(input):
    bit = input[0]
    number = input[1:5]
    input = input[5:]
    while bit == '1':
        bit = input[0]
        number += input[1:5]
        input = input[5:]
    return int(number, 2), input

def parse_op(input):
    # print(input)
    if input[0] == '0':
        # length 15
        length = int(input[1:16], 2)
        rest = input[16:16+length]
        print(f'op, l={length}')        
        result = []
        while len(rest) > 0:            
            op, rest = parse_code(rest)
            result.append(op)
        rest = input[16+length:]
    else:
        # length 11
        num = int(input[1:12], 2)
        rest = input[12:]
        print(f'op, n={num}')
        result = []
        for i in range(num):
            op, rest = parse_code(rest)
            result.append(op)
    return result, rest

def parse_code(input):
    print(input)
    version = int(input[:3], 2)
    versions.append(version)
    type = int(input[3:6], 2)
    print(version, type)
    if type == 4:
        result, rest = parse_number(input[6:])
    elif type != 4:
        result, rest = parse_op(input[6:])
        result
    return result, rest

versions = []
decoded, rest = parse_code(input)
print(decoded)
print(rest)
print(versions, sum(versions))