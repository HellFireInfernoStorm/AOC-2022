from string import ascii_lowercase as letters
from queue import Queue

start = ()

with open('input.txt') as f:
    grid = [[char for char in line] for line in f.read().splitlines()]

yMax = len(grid)
xMax = len(grid[0])

for y in range(yMax):
    for x in range(xMax):
        if grid[y][x] == 'S':
            grid[y][x] = 0
            continue
        if grid[y][x] == 'E':
            grid[y][x] = 25
            start = (x, y)
            continue
        grid[y][x] = letters.index(grid[y][x])

distances = [[-1 for x in range(xMax)] for y in range(yMax)]
visited = set()
pending = Queue()
distances[start[1]][start[0]] = 0
visited.add(start)
pending.put(start)

while not pending.empty():
    x, y = pending.get()
    height = grid[y][x]
    dist = distances[y][x]
    for nX, nY in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x1 = nX + x
        y1 = nY + y
        if x1 < 0 or y1 < 0 or x1 >= xMax or y1 >= yMax:
            continue
        if (x1, y1) in visited:
            continue
        if grid[y1][x1] < height -1:
            continue
        visited.add((x1, y1))
        distances[y1][x1] = dist + 1
        pending.put((x1, y1))
        if grid[y1][x1] == 0:
            print(distances[y1][x1])
            exit()