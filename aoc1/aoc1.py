

list1, list2 = zip(*[map(int, line.split()) for line in open('input.txt')])

# Part 1
print(sum(abs(a-b) for a,b in zip(sorted(list1), sorted(list2))))

# Part 2
print(sum(a * sum(a == b for b in list2) for a in list1))