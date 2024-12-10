data = [[int(x) for x in line.strip()] for line in open('aoc10/input.txt')]

n = len(data)
m = len(data[0])
dirs = [(0,1), (0,-1), (1,0), (-1,0)]
heads = [(i,j) for i in range(n) for j in range(m) if data[i][j] == 0]

def valid(i,j):
    return 0 <= i < n and 0 <= j < m

def score(i,j):
    locs = {(i,j)}
    for height in range(1,10):
        locs = {(i+di,j+dj) for (i,j) in locs for (di,dj) in dirs 
                if valid(i+di,j+dj) and data[i+di][j+dj] == height}
    return len(locs)

def rating(i,j):
    if data[i][j] == 9:
        return 1
    return sum(rating(i+di,j+dj) for (di,dj) in dirs
               if valid(i+di,j+dj) and data[i+di][j+dj] == data[i][j]+1)

print('Part 1:', sum(score(i,j) for (i,j) in heads))
print('Part 2:', sum(rating(i,j) for (i,j) in heads))