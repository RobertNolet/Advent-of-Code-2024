from itertools import product
from collections import defaultdict

with open('input.txt') as file:
    data = [list(line.strip()) for line in file]

n = len(data)
m = len(data[0])

i, j = next((i, j) for i, j in product(range(n), range(m)) if data[i][j] == '^')
di, dj = -1, 0

def run(i, j, di, dj):
    visited = defaultdict(set)
    while True:
        visited[(i,j)].add((di, dj))
        while 0 <= i+di < n and 0 <= j+dj < m and data[i+di][j+dj] == '#':
            di, dj = dj, -di
            visited[(i,j)].add((di,dj))
        i += di
        j += dj
        if not (0 <= i < n and 0 <= j < m):
            # We finished
            return visited, False
        if (di,dj) in visited[(i,j)]:
            # We're looping!
            return visited, True

visited, _ = run(i, j, di, dj)
print('Part 1:', len(visited))

result2 = 0
for row, col in visited.keys():
    if data[row][col] == '.':
        data[row][col] = '#'
        _, loop = run(i, j, di, dj)
        data[row][col] = '.'
        if loop:
            result2 += 1
print('Part 2:', result2)