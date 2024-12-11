from collections import defaultdict

with open('aoc11/input.txt') as file:
    data = {int(x):1 for x in file.readline().split()}

#data = [125, 17]

def blink(data):
    newdata = defaultdict(int)
    for x, count in data.items():
        n = len(str(x))
        if x == 0:
            newdata[1] += count
        elif n % 2 == 0:
            newdata[int(str(x)[:n//2])] += count
            newdata[int(str(x)[n//2:])] += count
        else:
            newdata[x*2024] += count
    return newdata

for b in range(25):
    data = blink(data)
print('Part 1:', sum(data.values()))

for b in range(50):
    data = blink(data)
print('Part 2:', sum(data.values()))