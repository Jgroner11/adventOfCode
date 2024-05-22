starting_numbers = [14,1,17,0,3,20]

mem = dict()

for i, x in enumerate(starting_numbers[:-1]):
    mem[x] = i + 1
    # print(x)
prev = starting_numbers[-1]
# print(prev)
for i in range(len(starting_numbers) + 1, 30000000 + 1):
    if prev not in mem:
        curr = 0
    else:
        curr = i-1 - mem[prev]
    mem[prev] = i - 1
    # print(curr)
    prev = curr

print(prev)