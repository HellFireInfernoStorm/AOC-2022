from string import ascii_lowercase as letters

start = ()
end = ()

with open('input.txt') as f:
    grid = [[char for char in line] for line in f.read().splitlines()]

yMax = len(grid)
xMax = len(grid[0])

for y in range(yMax):
    for x in range(xMax):
        if grid[y][x] == 'S':
            grid[y][x] = 0
            start = (x, y)
            continue
        if grid[y][x] == 'E':
            grid[y][x] = 25
            end = (x, y)
            continue
        grid[y][x] = letters.index(grid[y][x])

distances = [[-1 for x in range(xMax)] for y in range(yMax)]
distances[start[1]][start[0]] = 0

prev = [[(-1, -1) for x in range(xMax)] for y in range(yMax)]
visited = set()

def getShortestNode():
    x, y = -1, -1
    dist = 1e10
    for nY in range(yMax):
        for nX in range(xMax):
            if (nX, nY) in visited:
                continue
            if distances[nY][nX] == -1:
                continue
            if distances[nY][nX] < dist:
                x, y = nX, nY
                dist = distances[nY][nX]
    return (x, y)

def checkNeighbours(x, y):
    height = grid[y][x]
    dist = distances[y][x]
    visited.add((x, y))
    for nX, nY in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x1 = nX + x
        y1 = nY + y
        if x1 < 0 or y1 < 0 or x1 >= xMax or y1 >= yMax:
            continue
        if (x1, y1) in visited:
            continue
        if grid[y1][x1] > height+1:
            continue
        if 0 <= distances[y1][x1] <= dist+1:
            continue
        distances[y1][x1] = dist+1
        prev[y1][x1] = (x, y)

while len(visited) < xMax*yMax:
    x, y = getShortestNode()
    if (x, y) == (-1, -1):
        break
    checkNeighbours(x, y)

print(distances[end[1]][end[0]])