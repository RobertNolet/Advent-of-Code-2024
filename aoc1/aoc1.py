

list1, list2 = zip(*[map(int, line.split()) for line in open('input.txt')])

# Part 1
print("Part 1:", sum(abs(a-b) for a,b in zip(sorted(list1), sorted(list2))))

# Part 2
print("Part 2:", sum(a * list2.count(a) for a in list1))
