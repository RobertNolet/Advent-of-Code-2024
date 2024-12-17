import re
from itertools import product

pat = re.compile(r'(\d+)')

with open('input.txt') as file:
    (a, b, c), code = [[int(x) for x in pat.findall(block)]for block in file.read().split('\n\n')]

combo = lambda x, a, b, c: x if x < 4 else [a,b,c][x-4]
ops = {0: lambda op, i, a, b, c: (i+2, a//(2**combo(op, a, b, c)), b, c, None),
       1: lambda op, i, a, b, c: (i+2, a, b^op, c, None),
       2: lambda op, i, a, b, c: (i+2, a, combo(op, a, b, c)%8, c, None),
       3: lambda op, i, a, b, c: (i+2 if a == 0 else op, a, b, c, None),
       4: lambda op, i, a, b, c: (i+2, a, b^c, c, None),
       5: lambda op, i, a, b, c: (i+2, a, b, c, combo(op, a, b, c)%8),
       6: lambda op, i, a, b, c: (i+2, a, a//(2**combo(op, a, b, c)), c, None),
       7: lambda op, i, a, b, c: (i+2, a, b, a//(2**combo(op, a, b, c)), None)}

def singleout(i, a, b, c):
    while i < len(code):
        i, a, b, c, out = ops[code[i]](code[i+1], i, a, b, c)
        if out is not None:
            return i, a, b, c, out
    return i, a, b, c, None

def run(a, b, c):
    output = []
    i = 0
    while i < len(code):
        i, a, b, c, out = singleout(i, a, b, c)
        output.append(out)
    return [x for x in output if x is not None]

print('Part 1:', ','.join(map(str, run(a, b, c))))

possa = [0]
for x in reversed(code):
    newa = []
    for a3, pa in product(range(8), possa):        
        if run(pa*8+a3, b, c)[0] == x:
            newa.append(pa*8+a3)
    possa = newa

print('Part 2:', min(possa))