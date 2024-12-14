import re
from math import prod
import matplotlib.pyplot as plt
from itertools import count
pat = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')

data = [[int(s) for s in pat.match(line).groups()] for line in open('input.txt')]

#n,m = 7,11
n,m = 103, 101

quads = [0,0,0,0]
for px, py, vx, vy in data:
    x = (px + vx*100)%m
    y = (py + vy*100)%n
    if x < m//2 and y < n//2:
        quads[0] += 1
    elif x > m//2 and y < n//2:
        quads[1] += 1
    elif x < m//2 and y > n//2:
        quads[2] += 1
    elif x > m//2 and y > n//2:
        quads[3] += 1

print('Part 1:', prod(quads))

def hasstem(pts):
    xcount = [sum(px == x for px, py in pts) for x in range(m)]
    return max(xcount) > 20

for t in count():
    pts = {((px + t*vx)%m, (py + t*vy)%n) for px, py, vx, vy in data}
    if hasstem(pts):
        plt.plot(*zip(*pts), 'g.')
        plt.title(f'Time = {t}')
        plt.show()
        input()

