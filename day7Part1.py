def processLine(line):
    """take in string representing a bags contain statement and return a string of the initial color as well as a list of the strings of the other colors"""
    index1 = line.find(' bags contain ')
    key = line[:index1]

    if 'contain no other bags' in line:
        return key, []

    cutLine = line[index1 + len(' bags contain '):line.find('.')]
    processedLine = cutLine.split(', ')
    for i in range(len(processedLine)):
        processedLine[i] = processedLine[i][2:processedLine[i].find(' bag')]
    value = processedLine
    return key, value

def invertGraph(dictGraph):
    """take a dictionary representing a graph (where the value is a list of keys) and invert it
       returns a new dictionary such that every key in the new dictionary is an element of a value-list from the old dictionary and 
       the value of each key is a list of all the keys in the original graph which had that key in their value-list 
    """
    invertedGraph = dict()
    for key in dictGraph:
        invertedGraph[key] = []
        
    for key in dictGraph:
        for key_prime in dictGraph[key]:
            if key_prime not in invertedGraph:
                invertedGraph[key_prime] = [key]
            else:
                invertedGraph[key_prime].append(key)

    return invertedGraph    

def removeDuplicates(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res


def foo(key):
    l = bagGraph_prime[key]
    if l == []:
        return []
    for i in range(len(l)):
        l1 = foo(l[i])
        l.extend(l1)
    return l

def getNumOuterBags(bagColor):
    l = foo(bagColor)
    l = removeDuplicates(l)
    return len(l)


bagGraph = dict()

# process input and put color strings into bagGraph dictionary
with open('adventOfCode/day7Input.txt', 'r') as f:
    for line in f.readlines():
        key, value = processLine(line)
        bagGraph[key] = value

bagGraph_prime = invertGraph(bagGraph)

print(getNumOuterBags('shiny gold'))
