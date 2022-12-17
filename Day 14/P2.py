with open('input.txt') as f:
    data = [[[int(coord) for coord in point.split(',')] for point in line.split(' -> ')] for line in f.read().splitlines()]

yMax = 0
for line in data:
    for point in line:
        yMax = point[1] if point[1] > yMax else yMax
floor = yMax+2

lines = set()
for line in data:
    for i in range(len(line)-1):
        x1, y1 = line[i]
        x2, y2 = line[i+1]
        horizontal = True if y2 == y1 else False
        if horizontal:
            for x in range(min(x1, x2), max(x1, x2)+1):
                lines.add((x, y1))
        for y in range(min(y1, y2), max(y1, y2)+1):
            lines.add((x1, y))

sandSet = set()
sandOrigin = (500,0)

count = 0
while True:
    sand = sandOrigin
    while True:
        next = (sand[0], sand[1]+1)
        if next not in lines and next not in sandSet and next[1] < floor:
            sand = next
            continue
        next = (sand[0]-1, sand[1]+1)
        if next not in lines and next not in sandSet and next[1] < floor:
            sand = next
            continue
        next = (sand[0]+1, sand[1]+1)
        if next not in lines and next not in sandSet and next[1] < floor:
            sand = next
            continue
        sandSet.add(sand)
        break
    count += 1
    if sandOrigin in sandSet:
        break

print(count)