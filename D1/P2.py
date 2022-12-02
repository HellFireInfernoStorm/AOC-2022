vals = []
total = 0

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == '':
            vals.append(total)
            total = 0
            continue
        total += int(line)        

vals.sort(reverse=True)
print(sum(vals[:3]))