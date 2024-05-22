preambleLen = 25

def checkValid(num, l):
    n = len(l)
    for i in range(n):
        for j in range(n - (i + 1)):
            jshift = j + (i + 1)
            if(l[i] + l[jshift] == num):
                return True
    return False

currentList = list()

with open('adventOfCode/day9Input.txt', 'r') as f:
    while(len(currentList) < preambleLen):
        currentList.append(int(f.readline()))
    value = int(f.readline())

    while(checkValid(value, currentList)):
        currentList.pop(0)
        currentList.append(value)
        value = int(f.readline())

print(value)

sumDict = dict()
inputList = list()



with open('adventOfCode/day9Input.txt', 'r') as f:
    complete = False
    while not complete:
        i = int(f.readline())
        inputList.append(i)
        sumDict[i] = 0
        keysToDelete = list()
        for key in sumDict:
            sumDict[key] += i
            if sumDict[key] == value:
                correctKey = key
                complete = True
            elif sumDict[key] > value:
                keysToDelete.append(key)
        for key in keysToDelete:
            del sumDict[key]

valsList = inputList[inputList.index(correctKey):]

print(min(valsList) + max(valsList))
