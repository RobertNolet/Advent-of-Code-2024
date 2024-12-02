from itertools import pairwise

data = [list(map(int, line.split())) for line in open('input.txt')]

def diff(rep):
    return [(a-b) for a, b in pairwise(rep)]

def safe(rep):
    drep = diff(rep)
    return ((all(d > 0 for d in drep) or all(d < 0 for d in drep)) and
            all( 1 <= abs(d) <= 3 for d in drep))

# Part 1
print('Part 1:', sum(safe(rep) for rep in data))

# Part 2
print('Part 2:', sum(any(safe(rep[:i]+rep[i+1:]) for i in range(len(rep))) for rep in data))
