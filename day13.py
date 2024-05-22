from functools import reduce
import sympy as sp
import math

lst= []

with open('day13Input.txt', 'r') as f:
    line1 = f.readline().strip()
    line2 = f.readline().strip()

t = int(line1)
schedule = line2.split(',')

schedule_abridged = list(map(int, filter(lambda x: x != 'x', schedule)))

wait_times = list(map(lambda x: x - t % x, schedule_abridged))

wait_time = min(wait_times)
bus_id = schedule_abridged[wait_times.index(wait_time)]

print(wait_time * bus_id)


def check(schedule, t):
    for i, v in enumerate(schedule):
        if v != 'x':
            v = int(v)
            if (v - t % v) % v != i % v:
                return False
    return True

def chinese_remainder_thm(pairs):
    '''
    Solves system of modular equations:
        x = a1 mod b1
        x = a2 mod b2
        ...
    returns x mod N, where N = b1 * b2 * ...
    pairs is a list of tuples:
        [(a1, b1), (a2, b2), ...]
    '''
    N = reduce(lambda x, y: x * y, map(lambda x: x[1], pairs))

    acc = 0
    while pairs:
        (a, b) = pairs.pop()
        acc += (N // b) * sp.mod_inverse(N // b, b) * a

    return acc % N

pairs = []
for i, v in enumerate(schedule):
    if v != 'x':
        v = int(v)
        pairs.append((-i % v, v))

print(chinese_remainder_thm(pairs))

# i = math.lcm(*schedule_abridged)
