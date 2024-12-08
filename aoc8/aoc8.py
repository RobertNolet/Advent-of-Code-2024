from collections import defaultdict
from itertools import combinations, count

data = [line.strip() for line in open('aoc8/input.txt')]
n = len(data)
m = len(data[0])

def valid(i,j):
    return 0 <= i < n and 0 <= j < m

antennas = defaultdict(set)
for i, line in enumerate(data):
    for j, symbol in enumerate(line):
        if symbol != '.':
            antennas[symbol].add((i,j))

antinodes1 = set()
antinodes2 = set()
for locs in antennas.values():
    for (i1,j1), (i2,j2) in combinations(locs, 2):
        di = i2-i1
        dj = j2-j1
        for k in [-1,2]:
            if valid(i1+k*di, j1+k*dj):
                antinodes1.add((i1+k*di, j1+k*dj))
        for k in count():
            if not valid(i2+k*di, j2+k*dj):
                break
            antinodes2.add((i2+k*di, j2+k*dj))
        for k in count():
            if not valid(i1-k*di, j1-k*dj):
                break
            antinodes2.add((i1-k*di, j1-k*dj))
        
print('Part 1:', len(antinodes1))
print('Part 2:', len(antinodes2))
