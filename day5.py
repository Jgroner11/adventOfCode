def getBinaryDigit(c):
    if c == 'B' or c == 'R':
        return 1
    return 0
    

def sToB(s):
    l = len(s)
    if l == 1:
        return getBinaryDigit(s)
    i = getBinaryDigit(s[l - 1])
    return i + 10 * sToB(s[:l - 1])

def bToD(n):
    if n == 0:
        return n
    return (n % 10) + 2 * bToD(int(n / 10))

maxID = 0
lineNumber = 0

with open('adventOfCode/day5Input.txt', 'r') as f:
    for line in f.readlines():
        s = line[:line.find('/n')]
        b = sToB(s)
        d = bToD(b)

        if d > maxID:
            maxID = d

print('maxID', maxID)   

l = list()
for i in range(maxID):
    l.append(i + 1)


with open('adventOfCode/day5Input.txt', 'r') as f:
    for line in f.readlines():
        s = line[:line.find('/n')]
        b = sToB(s)
        d = bToD(b)
        l.remove(d)

print('my seatID', l[len(l) - 1])


# s = 'BBFBFFFRRL'
# b = sToB(s)
# d = bToD(b)

# sr = s[:7]
# br = sToB(sr)
# dr = bToD(br)

# sc = s[7:]
# bc = sToB(sc)
# dc = bToD(bc)

# print(s, b, d)