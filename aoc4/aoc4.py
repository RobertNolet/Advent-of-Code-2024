from itertools import product

data = [line.strip() for line in open('aoc4/input.txt')]

n = len(data)
m = len(data[0])

count1 = 0
count2 = 0
for i, j in product(range(n), range(m)):
    if data[i][j] == 'X':
        for di,dj in product([-1,0,1],[-1,0,1]):
            if (di,dj) != (0,0) and 0 <= i+3*di < n and 0 <= j+3*dj < m:
                if ''.join(data[i+k*di][j+k*dj] for k in range(4)) == 'XMAS':
                    count1 += 1
    if (data[i][j] == 'A' and 
        i not in (0,n-1) and 
        j not in (0,m-1) and
        ''.join(data[i+k][j+k] for k in [-1,0,1]) in ('MAS', 'SAM') and
        ''.join(data[i+k][j-k] for k in [-1,0,1]) in ('MAS', 'SAM')):
            count2 += 1


print('Part 1:', count1)
print('Part 2:', count2)