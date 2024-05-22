mem = {}
mask = 'X' * 36
# Len of all bin strings and all masks will be 36

def parse(line):
    lst = line.split(' = ')
    if lst[0] == 'mask':
        return ('mask', None, lst[1].rstrip())
    return('mem', int(line[line.index('[') + 1:line.index(']')]), int(lst[1].rstrip()))

def binS_to_dec(binS):
    if not binS:
        return 0
    return 2 * binS_to_dec(binS[:-1]) + int(binS[-1])

def dec_to_binS(dec):
    acc = []
    while dec:
        acc.append(str(dec % 2))
        dec //= 2
    return ''.join(acc[::-1])

def bitmask(binS, mask):
    acc = []
    
    for i, ch in enumerate(''.join(['0' * (len(mask) - len(binS)), binS])):
        match mask[i]:
            case 'X':
                acc.append(ch)
            case x:
                acc.append(x)
    return ''.join(acc)


with open('day14Input.txt', 'r') as f:
    for line in f.readlines():
        (type, key, val) = parse(line)
        if type == 'mask':
            mask = val
        else:
            mem[key] = bitmask(dec_to_binS(val), mask)

print(sum(map(binS_to_dec, list(mem.values()))))

# Part 2

def bitmask2(binS, mask):
    acc = []
    for i, ch in enumerate(''.join(['0' * (len(mask) - len(binS)), binS])):
        match mask[i]:
            case 'X':
                acc.append('X')
            case '0':
                acc.append(ch)
            case '1':
                acc.append('1')
    return ''.join(acc)
    
def floating_permutations(floating_address):
    acc = []
    def helper(s):
        pos = s.find('X')
        if pos == -1:
            acc.append(s)
        else:
            helper(s[:pos] + '0' + s[pos + 1:])
            helper(s[:pos] + '1' + s[pos + 1:])
    helper(floating_address)
    return acc

mem = {}
mask = '0' * 36

with open('day14Input.txt', 'r') as f:
    for line in f.readlines():
        (type, key, val) = parse(line)
        if type == 'mask':
            mask = val
        else:
            for address in floating_permutations(bitmask2(dec_to_binS(key), mask)):
                mem[address] = val

print(sum(list(mem.values())))