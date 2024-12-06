from itertools import pairwise

data = [list(map(int, line.split())) for line in open('input.txt')]

def safe(rep):
    drep = [(a-b) for a, b in pairwise(rep)]
    return all( -3 <= d <= -1 for d in drep) or all( 1 <= d <= 3 for d in drep)
            
# Part 1
print('Part 1:', sum(safe(rep) for rep in data))

# Part 2
print('Part 2:', sum(any(safe(rep[:i]+rep[i+1:]) for i in range(len(rep))) for rep in data))