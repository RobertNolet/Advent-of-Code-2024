from collections import defaultdict
from itertools import combinations

with open('input.txt') as file:
    block1, block2 = file.read().split('\n\n')

rules = defaultdict(set)
for rule in block1.split('\n'):
    before, after = map(int, rule.split('|'))
    rules[after] = rules[after] | {before}
docs = [[int(x) for x in line.split(',')] for line in block2.split('\n')]

def validorder(doc):
    for before, after in combinations(doc, 2):
        if after in rules[before]:
            # There is a rule of the form after|before
            return False
    return True

def reorder(doc):
    result = []
    while doc:
        # Find an n in doc which does not need to be after any other n in doc
        n = next(n for n in doc if not set(doc) & rules[n])
        doc.remove(n)
        result.append(n)
    return result
    
result1 = 0
result2 = 0
for doc in docs:
    if validorder(doc):
        result1 += doc[len(doc)//2]
    else:
        newdoc = reorder(doc)
        result2 += newdoc[len(newdoc)//2]
    

print('Part 1:', result1)
print('Part 2:', result2)


