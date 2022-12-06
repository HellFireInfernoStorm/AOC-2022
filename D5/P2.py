with open('input.txt') as f:
    data = f.read().splitlines()

stacks = {i : [] for i in range(1,10)}

for i in range(7,-1,-1):
    for j in range(1,10):
        c = data[i][j*4-3]
        if c != ' ':
            stacks[j].append(c)

for line in data[10:]:
    offset = line.find('from')
    n = int(line[5:offset-1])
    a = int(line[offset+5])
    b = int(line[offset+10])
    stacks[b].extend(stacks[a][-n::])
    stacks[a] = stacks[a][:-n]

word = ''
for i in range(1,10):
    word += stacks[i].pop()

print(word)