def processList(l):
    d = dict()
    for entry in l:

        # Remove '\n' if present
        indexNewLine = entry.find('\n')
        if indexNewLine != -1:
            entry = entry[:indexNewLine]
        
        # Add to dictionary d
        pair = entry.split(':')
        d.update({pair[0]:pair[1]})

    # Remove cid from dictionary
    if(d.get('cid', 0) != 0):
        d.pop('cid')
        
    return d


def checkValid(d):
    if len(d) != 7:
        print('len')
        return 0

    # byr (Birth Year)
    byr = int(d.pop('byr'))
    if not (1920 <= byr <= 2002):
        print('byr')
        return 0

    # iyr (Issue Year)
    iyr = int(d.pop('iyr'))
    if not (2010 <= iyr <= 2020):
        print('iyr')
        return 0

    # eyr (Expiration Year)
    eyr = int(d.pop('eyr'))
    if not (2020 <= eyr <= 2030):
        print('eyr')
        return 0

    # hgt (Height)
    hgt = d.pop('hgt')
    unit = hgt[len(hgt) - 2:]

    if unit == 'cm':
        val = int(hgt[:len(hgt) - 2])
        if not (150 <= val <= 193):
            print('hgt')
            return 0

    elif unit == 'in':
        val = int(hgt[:len(hgt) - 2])
        if not (59 <= val <= 76):
            print('hgt')
            return 0
    else:
        print('hgt')
        return 0
    
    # hcl (Hair Color)
    hcl = d.pop('hcl')
    if hcl[0] != '#':
        print('hcl')
        return 0
    if len(hcl) != 7:
        print('hcl')
        return 0
    for c in hcl[1:]:
        if not ((48 <= ord(c) <= 57) or (97 <= ord(c) <= 102)):
            print('hcl')
            return 0

    # ecl (Eye Color)
    ecl = d.pop('ecl')
    if not (ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'):
        print('ecl')
        return 0

    # pid (Passport ID)
    pid = d.pop('pid')
    if len(pid) != 9:
        print('pid')
        return 0
    
    print('valid')
    return 1

numValid = 0

l1 = list()
l2 = list()

with open('day4Input.txt', 'r') as f:  
    for line in f.readlines():
        if not (line == '\n'):
            l1 = line.split(' ')
            for entry in l1:
                l2.append(entry)
        else:
            print(processList(l2))
            numValid += checkValid(processList(l2))
            l2 = list()
        
print(numValid)
