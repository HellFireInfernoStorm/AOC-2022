rucksacks = []
total = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        c = len(line)//2
        rucksacks.append((set(line)))

for i in range(len(rucksacks)//3):
    c = ''.join(rucksacks[i*3].intersection(rucksacks[i*3+1], rucksacks[i*3+2]))
    if c.isupper():
        total += ord(c) - 38
        continue
    total += ord(c) - 96

print(total)