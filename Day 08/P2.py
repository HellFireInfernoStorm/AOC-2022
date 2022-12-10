grid = []
with open('input.txt') as f:
    for line in f:
        grid.append([int(char) for char in line.strip()])

xMax = len(grid[0]) - 1
yMax = len(grid) - 1

def scenicScore(x, y):
    dy1 = 1
    while (y - dy1) > 0:
        if grid[y-dy1][x] >= grid[y][x]:
            break
        dy1 += 1

    dy2 = 1
    while (y + dy2) < yMax:
        if grid[y+dy2][x] >= grid[y][x]:
            break
        dy2 += 1

    dx1 = 1
    while (x - dx1) > 0:
        if grid[y][x-dx1] >= grid[y][x]:
            break
        dx1 += 1

    dx2 = 1
    while (x + dx2) < xMax:
        if grid[y][x+dx2] >= grid[y][x]:
            break
        dx2 += 1

    return dy1 * dy2 * dx1 * dx2

highest = 0
for x in range(1, xMax):
    for y in range(1, yMax):
        s = scenicScore(x, y)
        if s > highest:
            highest = s

print(highest)