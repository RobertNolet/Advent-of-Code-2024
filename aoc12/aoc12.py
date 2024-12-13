from itertools import product


with open('aoc12/input.txt') as file:
    data = [line.strip() for line in file]

n = len(data)
m = len(data[0])
dirs = [(0,1), (1,0), (0,-1), (-1,0)]

def valid(i,j):
    return 0 <= i < n and 0 <= j < m

def neighbours(i,j,s):
    return {(i+di, j+dj) for (di,dj) in dirs if valid(i+di, j+dj) and data[i+di][j+dj] == s}

def cluster(points):
    groups = []
    while points:
        group = set()
        i,j = points.pop()
        s = data[i][j]
        tocheck = {(i,j)}
        points -= tocheck
        while tocheck:
            i,j = tocheck.pop()
            group.add((i,j))
            nbrs = neighbours(i,j,s)
            tocheck |= nbrs & points
            points -= nbrs
        groups.append(group)
    return groups

result1 = 0
result2 = 0
for group in cluster(set(product(range(n), range(m)))):
    fences = [{(i,j) for i,j in group 
               if not valid(i+di,j+dj) or 
               data[i+di][j+dj] != data[i][j]} for di, dj in dirs]
    result1 += len(group)*sum(map(len, fences))
    result2 += len(group)*sum(map(len, map(cluster, fences)))

print('Part 1:', result1)
print('Part 2:', result2)
