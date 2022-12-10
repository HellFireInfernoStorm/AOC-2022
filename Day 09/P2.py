class Knot():
    def __init__(self, pos, parent=None):
        self.pos = pos
        self.parent = parent
        self.child = None
        self.history = set()

    def updateHistoryRecursive(self):
        self.history.add((self.pos[0], self.pos[1]))
        if self.child != None:
            self.child.updateHistoryRecursive()

    def addChildRecursive(self):
        if self.child == None:
            self.child = Knot(pos = self.pos.copy(), parent = self)
            return
        self.child.addChildRecursive()

    def getTailRecursive(self):
        if self.child == None:
            return self
        return self.child.getTailRecursive()

    def followRecursive(self):
        if self.parent != None:
            dx = self.parent.pos[0] - self.pos[0]
            dy = self.parent.pos[1] - self.pos[1]
            if not (abs(dx) <= 1 and abs(dy) <= 1):
                self.pos[1] += dy//abs(dy) if dy != 0 else 0
                self.pos[0] += dx//abs(dx) if dx != 0 else 0
        if self.child != None:
            self.child.followRecursive()



head = Knot(pos=[0,0])
for i in range(1, 10):
    head.addChildRecursive()
head.updateHistoryRecursive()

guide = {'U':(1,1), 'D':(1,-1), 'L':(0,1), 'R':(0,-1)}
def moveHead(dir, count):
    axis, inc = guide[dir]
    for i in range(count):
        head.pos[axis] += inc
        head.followRecursive()
        head.updateHistoryRecursive()

with open('input.txt') as f:
    for line in f:
        line = line.strip().split()
        dir = line[0]
        count = int(line[1])
        moveHead(dir, count)

print(len(head.getTailRecursive().history))