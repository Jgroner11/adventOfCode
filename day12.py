import numpy as np


def part1():
    x = 0
    y = 0
    dir = 0
    compass = ['E', 'S', 'W', 'N']

    def move(instruction, dist):
        nonlocal x, y, dir

        match instruction:
            case 'E':
                x += dist
            case 'S':
                y -= dist
            case 'W':
                x -= dist
            case 'N':
                y += dist
            case 'F':
                return move(compass[dir], dist)
            case 'R':
                dir = (dir + dist // 90) % 4
            case 'L':
                dir = (dir - dist // 90) % 4        

    for line in lst:
            move(line[0], int(line[1:]))
    print(abs(x) + abs(y))

def part2():
    x = 0
    y = 0

    way = np.array((10, 1))

    rotation_matrix = [np.array(((1, 0), (0, 1))), np.array(((0, 1), (-1, 0))), np.array(((-1, 0), (0, -1))), np.array(((0, -1), (1, 0)))] 

    for line in lst:
        instruction, dist = line[0], int(line[1:])
        match instruction:
            case 'E':
                way[0] += dist
            case 'S':
                way[1] -= dist
            case 'W':
                way[0] -= dist
            case 'N':
                way[1] += dist
            case 'F':
                (x, y) = (x, y) + dist * way
            case 'R':
                way = rotation_matrix[dist // 90] @ way
            case 'L':
                way = rotation_matrix[4 - dist // 90] @ way

    print(abs(x) + abs(y))



lst = []
with open('day12Input.txt', 'r') as f:
    for line in f.readlines():
        lst.append(line[:len(line) - 1])


# part1()

part2()
