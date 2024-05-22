l = list()
with open('adventOfCode/day10Input.txt', 'r') as f:
    for line in f.readlines():
        l.append(int(line))


l.sort()
l.insert(0, 0)
l.append(l[len(l) - 1] + 3)

num1JDif = 0
num3JDif = 0

i = 0
while i < len(l) - 1:
    x = l[i + 1] - l[i]
    if x == 1:
        num1JDif += 1
    elif x == 3:
        num3JDif += 1
    i += 1
print(num1JDif * num3JDif)

d = dict()

for i in range(len(l)):
    l1 = list()
    j = i - 1
    while j >= 0 and l[j] >= l[i] - 3:
        l1.append(d[l[j]])
        j -= 1
    if len(l1) == 0:
        d[l[i]] = 1
    else:
        d[l[i]] = sum(l1)
    
print(d[l[len(l) - 1]])