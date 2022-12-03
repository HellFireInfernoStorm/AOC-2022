rucksacks = []
total = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        c = len(line)//2
        rucksacks.append((set(line[:c]), set(line[c:])))

for rucksack in rucksacks:
    c = ''.join(rucksack[0].intersection(rucksack[1]))
    if c.isupper():
        total += ord(c) - 38
        continue
    total += ord(c) - 96

print(total)