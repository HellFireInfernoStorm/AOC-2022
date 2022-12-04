data = []
count = 0

with open('input.txt') as f:
    for line in f:
        line = [[int(n) for n in pair.split('-')] for pair in line.strip().split(',')]
        data.append(line)

for line in data:
    a, b = line[0][0], line[0][1]
    c, d = line[1][0], line[1][1]
    if (a>c and b>d) or (a<c and b<d):
        continue
    count += 1

print(count)