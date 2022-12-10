max = total = 0

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line == '':
            if total > max:
                max = total
            total = 0
            continue
        total += int(line)        

print(max)