with open('input.txt') as f:
    data = f.read().splitlines()

stacks = {i : [] for i in range(1,10)}

for i in range(7,-1,-1):
    for j in range(1,10):
        c = data[i][j*4-3]
        if c != ' ':
            stacks[j].append(c)

for line in data[10:]:
    i = line.find('from')
    n = int(line[5:i-1])
    a = int(line[i+5])
    b = int(line[i+10])
    for i in range(n):
        stacks[b].append(stacks[a].pop())

word = ''
for i in range(1,10):
    word += stacks[i].pop()

print(word)