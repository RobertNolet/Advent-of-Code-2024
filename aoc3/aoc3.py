import re

with open('input.txt') as file:
    data = file.read()

pat = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")
ops = pat.findall(data)

res1 = 0
res2 = 0
enabled = 1
for op in ops:
    if op == "do()":
        enabled = 1
    elif op == "don't()":
        enabled = 0
    elif op[:4] == "mul(":
        a, b = op[4:-1].split(',')
        res1 += int(a)*int(b)
        res2 += int(a)*int(b)*enabled
    else:
        print("Unexpected op!")

print("Part 1:", res1)
print("Part 2:", res2)

