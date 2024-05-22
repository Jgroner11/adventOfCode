sum = 0

l1 = []
l2 = []

with open('adventOfCode/day6Input.txt', 'r') as f:
    for line in f.readlines():
        if line != '\n':
            l1.append(line[:len(line) - 1])
        else:
            for entry in l1:
                for c in entry:
                    if not c in l2:
                        l2.append(c)
            sum += len(l2)

            l1 = list()
            l2 = list()

print(sum)

sum = 0

l1 = []
l2 = []

with open('adventOfCode/day6Input.txt', 'r') as f:
    for line in f.readlines():
        if line != '\n':
            l1.append(line[:len(line) - 1])
        else:
            firstRun = True
            for entry in l1:
                if firstRun:          
                    for c in entry:
                        l2.append(c)
                    firstRun = False
                else:
                    l3 = list()
                    for c in l2:
                        if not (c in entry):
                            l3.append(c)
                    for c in l3:
                        l2.remove(c)
            sum += len(l2)
            l1 = list()
            l2 = list()
print(sum)

# sum = 0
# l1 = []
# l2 = []
# 
# with open('adventOfCode/day6Input.txt', 'r') as f:
#     for line in f.readlines():
#         if line != '\n':
#             l1.append(line[:len(line) - 1])
#         else:
#             print('l1', l1, '\n')
#             firstRun = True
#             for entry in l1:
#                 if firstRun:
#                     print('firstRun')          
#                     for c in entry:
#                         l2.append(c)
#                     firstRun = False
#                     print('l2', l2)
#                     print('\n')
#                 else:
#                     print(entry)
#                     remove = list() # elements to be removed
#                     for c in l2:
#                         print(c, c in entry)
#                         if not (c in entry):
#                             remove.append(c)
#                             print(c + ' added to l3')
#                     for c in remove:
#                         print(c + ' removed from l2')
#                         l2.remove(c)
#                     print('l2', l2)
#                     print('\n')    
#             sum += len(l2)
#             print('l2', l2, len(l2), '\n')
#             l1 = list()
#             l2 = list()
# print(sum)