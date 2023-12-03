class snailfish_number():    
    
    def __init__(self, s):
        self.values = []
        self.levels = []
        self.parse(s)
    
    def parse(self, s):
        l = 0
        for c in s:
            if c == '[':
                l += 1
            elif c == ']':
                l -= 1
            elif c .isdigit():
                self.values.append(int(c))
                self.levels.append(l)

    def print(self):
        val = self.values.copy()
        lev = self.levels.copy()
        
        s = self._print(val, lev)
        print(s)
        
    def _print(self, val, lev):
        if len(val) == 1:
            return f'{val[0]}'
        maxlevel = max(lev)
        pos = lev.index(maxlevel)
        if lev[pos+1] != maxlevel:
            raise(f'Wrong levels: pos={pos}, lev={lev}')
        else:
            val = val[:pos] + [f'[{val[pos]},{val[pos+1]}]'] + val[pos+2:]
            lev = lev[:pos] + [lev[pos]-1] + lev[pos+2:]
            return self._print(val, lev)
                
    def reduce(self):        
        if max(self.levels)>4:
            # explode
            left = self.levels.index(5)
            right = left+1    
            # print(f' exploding: {self.values[left:left+2]} with levels {self.levels[left:left+2]}')
            if left>0:
                self.values[left-1] += self.values[left]
            if right+1<len(self.values):
                self.values[right+1] += self.values[right]
            self.values = self.values[:left] + [0] + self.values[right+1:]
            self.levels = self.levels[:left] + [4] + self.levels[right+1:]
            self.reduce()
        elif max(self.values)>9:
            # split
            pos = 0
            for v in self.values:
                if v>9:
                    break
                else:
                    pos += 1
            # print(f' splitting {self.values[pos]} with level {self.levels[pos]}')
            left = int(self.values[pos]/2)
            right = int((self.values[pos]+1)/2)
            level = self.levels[pos]+1
            self.values = self.values[:pos] + [left, right] + self.values[pos+1:]
            self.levels = self.levels[:pos] + [level]*2 + self.levels[pos+1:]
            self.reduce()
            
    def add(self, other):
        self.values += other.values
        self.levels += other.levels
        for i in range(len(self.levels)):
            self.levels[i] += 1
             
    def equal(self, other):
        if len(self.values) == len(other.values):
            eq = True
            for i in range(len(self.values)):
                eq = eq and self.values[i]==other.values[i] and self.levels[i]==other.levels[i]
        else:
            eq = False
        return eq
    
    def get_magnitude(self):
        val = self.values.copy()
        lev = self.levels.copy()
        
        return self._mag(val, lev)
        
    def _mag(self, val, lev):
        if len(val) == 1:
            return val[0]
        maxlevel = max(lev)
        pos = lev.index(maxlevel)
        if lev[pos+1] != maxlevel:
            raise(f'Wrong levels: pos={pos}, lev={lev}')
        else:
            val = val[:pos] + [3*val[pos]+2*val[pos+1]] + val[pos+2:]
            lev = lev[:pos] + [lev[pos]-1] + lev[pos+2:]
            return self._mag(val, lev)
                

with open('input.txt') as f:
    numbers = [line.strip() for line in f.readlines()]
    
n = snailfish_number(numbers[0])
for next in numbers[1:]:
    n.add(snailfish_number(next))
    n.reduce()

print('final result is:')
n.print()
# result of test.txt
# print(n.equal(snailfish_number('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')))
# result of test1.txt
# print('correct result of test1.txt? ', n.equal(snailfish_number('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')))
print(f'magnitude of the result: {n.get_magnitude()}')

print()
max_mag = []
max_mag_num = []
for i in range(len(numbers)):
    mag = []
    for j in range(len(numbers)):
        n = snailfish_number(numbers[i])
        n.add(snailfish_number(numbers[j]))
        n.reduce()
        mag.append(n.get_magnitude())
    max_mag.append(max(mag))
    max_mag_num.append(mag.index(max(mag)))
print(f'maximal magnitude obtainable by adding two numbers: {max(max_mag)}')
which = max_mag.index(max(max_mag))
print(numbers[which]+' + '+numbers[max_mag_num[which]])
# print(max_mag_num)

