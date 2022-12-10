count = 0

with open('input.txt') as f:
    for line in f:
        line = [[int(n) for n in pair.split('-')] for pair in line.strip().split(',')]
        a, b = line[0][0], line[0][1]
        c, d = line[1][0], line[1][1]
        if a>d or c>b:
            continue
        count += 1

print(count)