import numpy as np

with open('aoc9/input.txt') as file:
    data = file.readline().strip()

files = [int(x) for x in data[::2]]
free = [int(x) for x in data[1::2]]

n = sum(files)+sum(free)
disk = np.zeros(shape = n, dtype=int)
pfile = [0]
pfree = []

pos = files[0]
for i, (lfile, lfree) in enumerate(zip(files[1:], free)):
    pfree.append(pos)
    pos += lfree
    disk[pos:pos+lfile] = i+1
    pfile.append(pos)
    pos += lfile

lpos = files[0]
rpos = pos-1
while lpos < rpos:
    disk[lpos] = disk[rpos]
    disk[rpos] = 0
    lpos += 1
    while disk[lpos] != 0:
        lpos += 1
    rpos -= 1
    while disk[rpos] == 0:
        rpos -= 1

print('Part 1:', np.dot(np.arange(n),disk))

for i in reversed(range(len(files))):
    for j in range(len(free)):
        if free[j] >= files[i] and pfile[i] > pfree[j]:
            free[j] -= files[i]
            pfile[i] = pfree[j]
            pfree[j] += files[i]
            break

result = 0
for id, (lfile, pos) in enumerate(zip(files, pfile)):
    result += lfile*(2*pos+lfile-1)*id//2

print('Part 2:', result)