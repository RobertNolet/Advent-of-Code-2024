import re

pat = re.compile(r'(\d+)')
data = [list(map(int, pat.findall(line))) for line in open('input.txt')]

ops = {0:lambda x, y: x+y, 
       1:lambda x, y: x*y,
       2:lambda x, y: int(str(x)+str(y))}

def valid(value, start, terms, base):
    if start > value:
        return False
    if not terms:
        return value == start
    for b in range(base):
        if valid(value, ops[b](start, terms[0]), terms[1:], base):
            return True
    return False
        
result1 = 0
result2 = 0
for line in data:
    if valid(line[0], line[1], line[2:], 2):
        result1 += line[0]
    if valid(line[0], line[1], line[2:], 3):
        result2 += line[0]

print('Part 1:', result1)
print('Part 2:', result2)


