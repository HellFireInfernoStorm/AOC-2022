grid = []
with open('input.txt') as f:
    for line in f:
        grid.append([[int(char), False] for char in line.strip()])

xMax = len(grid[0])
yMax = len(grid)

for y in range(yMax):
    grid[y][0][1] = True
    grid[y][-1][1] = True
    tallest = grid[y][0][0]
    for x in range(1, xMax):
        if tallest == 9:
            break
        if grid[y][x][0] <= tallest:
            continue
        tallest = grid[y][x][0]
        grid[y][x][1] = True

    tallest = grid[y][-1][0]
    for x in range(-2, -(xMax+1), -1):
        if tallest == 9:
            break
        if grid[y][x][0] <= tallest:
            continue
        tallest = grid[y][x][0]
        grid[y][x][1] = True

for x in range(xMax):
    grid[0][x][1] = True
    grid[-1][x][1] = True
    tallest = grid[0][x][0]
    for y in range(1, yMax):
        if tallest == 9:
            break
        if grid[y][x][0] <= tallest:
            continue
        tallest = grid[y][x][0]
        grid[y][x][1] = True

    tallest = grid[-1][x][0]
    for y in range(-2, -(yMax+1), -1):
        if tallest == 9:
            break
        if grid[y][x][0] <= tallest:
            continue
        tallest = grid[y][x][0]
        grid[y][x][1] = True

count = 0
for y in range(yMax):
    for x in range(xMax):
        if grid[y][x][1]:
            count += 1

print(count)