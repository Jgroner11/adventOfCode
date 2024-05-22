def processLine(line):
    """take in string representing a bags contain statement and return a string of the initial color as well as a list of the strings of the other colors"""
    index1 = line.find(' bags contain ')
    key = line[:index1]

    if 'contain no other bags' in line:
        return key, []

    cutLine = line[index1 + len(' bags contain '):line.find('.')]
    processedLine = cutLine.split(', ')
    for i in range(len(processedLine)):
        processedLine[i] = [processedLine[i][2:processedLine[i].find(' bag')], int(processedLine[i][0])]
        
    value = processedLine
    return key, value

def foo(key):
    l = bagGraph[key]
    sum = 0
    for i in range(len(l)): 
        sum += l[i][1] * (1 + foo(l[i][0]))
    return sum

def getNumInnerBags(bagColor):
    i = foo(bagColor)
    return i

bagGraph = dict()
with open('adventOfCode/day7Input.txt', 'r') as f:
    for line in f.readlines():
        key, value = processLine(line)
        bagGraph[key] = value

print(getNumInnerBags('shiny gold'))