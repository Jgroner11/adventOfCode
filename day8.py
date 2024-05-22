acc = 0
visitedNodes = list()
commandList = list()

def commandToInt(s):
    if s == 'acc':
        return 1
    if s == 'jmp':
        return 2
    return 0


with open('adventOfCode/day8Input.txt', 'r') as f:
    for line in f.readlines():
        l =list()
        l.append(commandToInt(line[:3]))
        l.append(int(line[4:-1]))
        commandList.append(l)

length = len(commandList)


def foo(index2, acc2, visitedNodes2):
    while index2 not in visitedNodes2:
        if index2 == length:
            return acc2
        else:
            visitedNodes2.append(index2)
            l = commandList[index2]
            if l[0] == 1:
                acc2 += l[1]
                index2 += 1
            elif l[0] == 2:
                index2 += l[1]
            else:
                index2 += 1
    return 'null'

index = 0
finalAcc = 'null'
while finalAcc == 'null':
    visitedNodes.append(index)
    l = commandList[index]
    if l[0] == 1:
        acc += l[1]
        index += 1
    elif l[0] == 2:
        finalAcc = foo(index + 1, acc, visitedNodes)
        index += l[1]
    else:
        finalAcc = foo(index + l[1], acc, visitedNodes)
        index += 1


print(finalAcc)   
