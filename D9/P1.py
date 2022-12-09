head = [0, 0]
tail = [0, 0]
tailPos = set()
tailPos.add((tail[0], tail[1]))

def moveTail():
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if -1 <= dx <= 1 and -1 <= dy <= 1:
        return
    tail[1] += dy//abs(dy) if dy != 0 else 0
    tail[0] += dx//abs(dx) if dx != 0 else 0
    tailPos.add((tail[0], tail[1]))

guide = {'U':(1,1), 'D':(1,-1), 'L':(0,1), 'R':(0,-1)}
def moveHead(dir, count):
    axis, inc = guide[dir]
    for i in range(count):
        head[axis] += inc
        moveTail()

with open('input.txt') as f:
    for line in f:
        line = line.strip().split()
        dir = line[0]
        count = int(line[1])
        moveHead(dir, count)

print(len(tailPos))