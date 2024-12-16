dirs = [(0,1), (1,0), (0,-1), (-1,0)]

unvisited = set()
visited = {}
for i, line in enumerate(open('input.txt')):
    for j, c in enumerate(line):
        if c == '.':
            unvisited.update({(i,j,k) for k in range(4)})
        if c == 'S':
            visited[(i,j,0)] = 0
            unvisited.update({(i,j,k) for k in range(1,4)})
            current = (i,j,0)
            curdist = 0
        if c == 'E':
            unvisited.update({(i,j,k) for k in range(4)})
            dest = (i,j)

tocheck = {}
def addcheck(i,j,k,dist):
    if (i,j,k) in unvisited and tocheck.get((i,j,k), dist+1) > dist:
        tocheck[(i,j,k)] = dist

i, j, k = current
while unvisited:
    di, dj = dirs[k]
    addcheck(i, j, (k+1)%4, curdist+1000)
    addcheck(i, j, (k-1)%4, curdist+1000)
    addcheck(i+di, j+dj, k, curdist+1)    

    curdist, (i,j,k) = min(((dist, node) for node, dist in tocheck.items()))
    tocheck.pop((i,j,k))
    unvisited.remove((i,j,k))
    visited[(i,j,k)] = curdist

mindist = min(visited[dest + (k,)] for k in range(4))
print('Part 1:', mindist)

onroute = set()
tocheck = {dest+(k,) for k in range(4) if visited[dest+(k,)] == mindist}
while tocheck:
    i,j,k = tocheck.pop()
    onroute.add((i,j))
    dist = visited[(i,j,k)]
    di, dj = dirs[(k+2)%4]
    if visited.get((i+di, j+dj, k), dist) == dist-1:
        tocheck.add((i+di, j+dj, k))
    if visited.get((i, j, (k+1)%4), dist) == dist-1000:
        tocheck.add((i, j, (k+1)%4))
    if visited.get((i, j, (k-1)%4), dist) == dist-1000:
        tocheck.add((i, j, (k-1)%4))

print('Part 2:', len(onroute))
