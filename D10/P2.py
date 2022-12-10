with open('input.txt') as f:
    data = f.read().splitlines()

x = 1
history = [1]

for line in data:
    history.append(x)
    if line.startswith('n'):
        continue
    v = int(line.split(' ')[1])
    x += v
    history.append(x)

screen = [[' ' for j in range(40)] for i in range(6)]

for i in range(40*6):
    if not (-1 <= (i%40 - history[i]) <= 1):
        continue
    screen[i//40][i%40] = '█'

for i in range(6):
    for j in range(40):
        print(screen[i][j], end='')
        print(screen[i][j], end='')
    print('')