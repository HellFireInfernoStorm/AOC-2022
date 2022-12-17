with open('input.txt') as f:
    data = [[[int(coord) for coord in point.split(',')] for point in line.split(' -> ')] for line in f.read().splitlines()]

yMax = 0
for line in data:
    for point in line:
        yMax = point[1] if point[1] > yMax else yMax

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
flowingAbyss = False
while True:
    sand = sandOrigin
    while True:
        if sand[1] > yMax:
            flowingAbyss = True
            break
        next = (sand[0], sand[1]+1)
        if next not in lines and next not in sandSet:
            sand = next
            continue
        next = (sand[0]-1, sand[1]+1)
        if next not in lines and next not in sandSet:
            sand = next
            continue
        next = (sand[0]+1, sand[1]+1)
        if next not in lines and next not in sandSet:
            sand = next
            continue
        sandSet.add(sand)
        break
    if flowingAbyss:
        break
    count += 1

print(count)