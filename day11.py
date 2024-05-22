l1 = list()
newState = list()

def getNumAdjacent(state, index1, index2):
    numAdjacent = 0
    for i in range(3):
        for j in range(3):
            if (index1 - 1 + i >= 0 and index1 - 1 + i < len(state)):
                if(index2 - 1 + j >= 0 and index2 -1 + j < len(state[i])):
                    if(not(i == 1 and j == 1)):
                        if(state[index1 - 1 + i][index2 - 1 + j] == "#"):
                            numAdjacent += 1
    return numAdjacent


with open('day11Input.txt', 'r') as f:
    for line in f.readlines():
        l1.append(line[:len(line) - 1])

while(l1 != newState):
    newState = list()
    i = 0
    for line in l1:
        s = ""
        j = 0
        for element in line:
            if(element == "L" and getNumAdjacent(l1, i, j) == 0):
                s += "#"
            elif(element == "#" and getNumAdjacent(l1, i, j) >= 4):
                s += "L"
            else:
                s += element
            j += 1
        newState.append(s)
        i += 1
        
    temp = l1
    l1 = newState
    newState = temp

numOccupied = 0
for line in l1:
    for element in line:
        if(element == '#'):
            numOccupied += 1
print(numOccupied)


# Part 2
def getNumAdjacent2(state, index1, index2):
    numAdjacent = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(not(i == 0 and j == 0)):
                end = False
                k = 1
                while(not end):
                    if (index1 + i * k >= 0 and index1 + i * k < len(state) and index2 + j * k >= 0 and index2 + j * k < len(state[0])):
                        if(state[index1 + i * k][index2 + j * k] == "#"):
                            numAdjacent += 1
                            end = True
                        elif(state[index1 + i * k][index2 + j * k] == "L"):
                            end = True
                    else:
                        end = True
                    k += 1
    return numAdjacent

l1 = list()
newState = list()

with open('day11Input.txt', 'r') as f:
    for line in f.readlines():
        l1.append(line[:len(line) - 1])

while(l1 != newState):
    newState = list()
    i = 0
    for line in l1:
        s = ""
        j = 0
        for element in line:
            if(element == "L" and getNumAdjacent2(l1, i, j) == 0):
                s += "#"
            elif(element == "#" and getNumAdjacent2(l1, i, j) >= 5):
                s += "L"
            else:
                s += element
            j += 1
        newState.append(s)
        i += 1
        
    temp = l1
    l1 = newState
    newState = temp

numOccupied = 0
for line in l1:
    for element in line:
        if(element == '#'):
            numOccupied += 1
print(numOccupied)