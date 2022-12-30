def S2d(c):
    if c == '=':
        return -2
    elif c == '-':
        return -1
    else:
        return int(c)

def SNAFU2dec(snafu):
    number = 0
    for c in snafu:
        number = 5*number+S2d(c)
    return(number)


def dec2pen(d):
    r = d % 5
    n = d // 5
    if n == 0:
        return str(r)
    else:
        return dec2pen(n)+str(r)
    
def pen2SNAFU(p):
    SNAFU = ''
    plus = 0
    for d in reversed(p):
        c = int(d)+plus
        if c <= 2:
            SNAFU += str(c)
            plus = 0
        else:
            plus = 1
            if c == 3:
                SNAFU += '='
            elif c == 4:
                SNAFU += '-'
            elif c == 5:
                SNAFU += '0'
            else:
                print(f'IDK {c}')
    return ''.join([x for x in reversed(SNAFU)])

def dec2SNAFU(d):
    return pen2SNAFU(dec2pen(d))

s = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        SNAFU = line.strip()
        d = SNAFU2dec(SNAFU)
        s += d
        print(f' {SNAFU} {d}')
print(f'sum: {s} {dec2SNAFU(s)}')
        