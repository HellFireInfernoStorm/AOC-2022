with open('input.txt') as f:
    data = f.read().splitlines()

x = 1
history = [1, 1]

for line in data:
    history.append(x)
    if line.startswith('n'):
        continue
    v = int(line.split(' ')[1])
    x += v
    history.append(x)

total = 0
for i in [20, 60, 100, 140, 180, 220]:
    total += i * history[i]

print(total)