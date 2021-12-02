import re

def check_passport(string):
    keys = [k.split(':')[0] for k in string.split()]
    return set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']).issubset(set(keys))

def check_passport2(string):
    data = {k.split(':')[0]:k.split(':')[1] for k in string.split()}
    valid = False
    if set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']).issubset(set(data.keys())):
        valid = True
        # byr
        if (re.match('[0-9]{4}', data['byr'])):
            if (1920 <= int(data['byr'])) and  (int(data['byr']) <= 2002):
                pass
            else:
                valid = False
        else:
            valid = False
            
        # iyr
        if (re.match('[0-9]{4}', data['iyr'])):
            if (2010 <= int(data['iyr'])) and  (int(data['iyr']) <= 2020):
                pass
            else:
                valid = False
        else:
            valid = False
        
        # eyr
        if (re.match('[0-9]{4}', data['eyr'])):
            if (2020 <= int(data['eyr'])) and  (int(data['eyr']) <= 2030):
                pass
            else:
                valid = False
        else:
            valid = False

        # hgt
        if (re.match('[0-9]*[i,c][n,m]', data['hgt'])):
            unit = data['hgt'][-2:]
            value = int(data['hgt'][:-2])
            if (unit == 'in' and 59 <= value and value<= 76) or (unit == 'cm' and 150 <= value and value<= 193):
                pass
            else:
                valid = False
        else:
            valid = False
        
        # hcl
        if (re.match('#[0-9,a-f]{6}', data['hcl'])) and (len(data['hcl'])==7):
            pass
        else:
            valid = False
        
        # ecl
        if data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            pass
        else:
            valid = False
            
        # pid
        if (re.match('[0-9]{9}', data['pid'])) and (len(data['pid'])==9):
            pass
        else:
            valid = False
    return valid

def check_passport3(string):
    data = {k.split(':')[0]:k.split(':')[1] for k in string.split()}
    valid = False
    if set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']).issubset(set(data.keys())):
        valid = True
        # byr
        if re.match('[0-9]{4}$', data['byr']) and (1920 <= int(data['byr'])) and  (int(data['byr']) <= 2002):
            pass
        else:
            valid = False
            
        # iyr
        if re.match('[0-9]{4}$', data['iyr']) and (2010 <= int(data['iyr'])) and  (int(data['iyr']) <= 2020):
            pass
        else:
            valid = False
        
        # eyr
        if re.match('[0-9]{4}$', data['eyr']) and (2020 <= int(data['eyr'])) and  (int(data['eyr']) <= 2030):
            pass
        else:
            valid = False

        # hgt
        if (re.match('[0-9]*[i,c][n,m]$', data['hgt'])):
            unit = data['hgt'][-2:]
            value = int(data['hgt'][:-2])
            if (unit == 'in' and 59 <= value and value<= 76) or (unit == 'cm' and 150 <= value and value<= 193):
                pass
            else:
                valid = False
        else:
            valid = False
        
        # hcl
        if re.match('#[0-9,a-f]{6}$', data['hcl']):
            pass
        else:
            valid = False
        
        # ecl
        if data['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            pass
        else:
            valid = False
            
        # pid
        if re.match('[0-9]{9}$', data['pid']):
            pass
        else:
            valid = False
    return valid

input = open('4.in', 'r')
passport = ''
valid = 0

for line in input.readlines():
    line = line.rstrip()
    if line == '':
        if check_passport3(passport):
            valid += 1
        passport = ''
    else:
        passport += ' '+line
if passport != '':
    if check_passport3(passport):
        valid += 1
input.close()

print(valid)