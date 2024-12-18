import sys
sys.path.append('..')

from itertools import product
from tools.dijkstra import Dijkstra

data = [tuple(int(x) for x in line.split(',')) for line in open('input.txt')]
n = 70
nbytes = 1024

nodes = set(product(range(n+1), range(n+1))) - set(data[:nbytes])
dirs = [(0,1), (0,-1), (1,0), (-1,0)]

def nbrs(node):
    return {(node[0]+di,node[1]+dj) for di, dj in dirs} & nodes

print('Part 1:', Dijkstra(nodes, nbrs, 1).mindist((0,0), (n,n)))

lower = nbytes
upper = len(data)
while upper - lower > 1:
    m = (upper + lower) // 2
    nodes = set(product(range(n+1), range(n+1))) - set(data[:m])
    d = Dijkstra(nodes, nbrs, 1).mindist((0,0), (n,n))
    if d is None:
        upper = m
    else:
        lower = m

print(f'Part 2: {data[upper-1][0]},{data[upper-1][1]}')