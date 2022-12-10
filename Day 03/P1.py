from string import ascii_letters as letters

rucksacks = []
total = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        c = len(line)//2
        rucksacks.append((set(line[:c]), set(line[c:])))

for rucksack in rucksacks:
    c = ''.join(rucksack[0].intersection(rucksack[1]))
    total += letters.index(c) + 1

print(total)