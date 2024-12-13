import re

pat = re.compile(r'(\d+)')

with open('aoc13/input.txt') as file:
    data = [[map(int, pat.findall(line)) for line in block.split('\n')] for block in file.read().split('\n\n')]

def solve(ax, ay, bx, by, px, py):
    d = ax*by-bx*ay
    if (by*px - bx*py) % d == 0 and (ax*py - ay*px) % d == 0:
        return 3*(by*px - bx*py) // d + (ax*py - ay*px) // d 
    return 0

result1 = 0
result2 = 0
for (ax, ay), (bx, by), (px, py) in data:
    result1 += solve(ax, ay, bx, by, px, py)
    result2 += solve(ax, ay, bx, by, px+10000000000000, py+10000000000000)


print('Part 1:', result1)
print('Part 2:', result2)