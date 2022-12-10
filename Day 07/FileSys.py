class FileNode():
    def __init__(self, name, parent=None, dir=False, size=0):
        self.name = name
        self.parent = parent
        if dir:
            self.type = 'DIR'
            self.children = []
        else:
            self.type = 'FILE'
            self.size = size
    
    def setSize(self, size):
        self.size = size

    def addChild(self, child):
        self.children.append(child)
    
    def getParent(self):
        return self.parent
    
    def getChildren(self):
        return self.children

    def getChildDir(self, childName):
        for child in self.children:
            if childName == child.name and child.type == 'DIR':
                return child

        child = FileNode(name=childName, parent=self, dir=True)
        self.addChild(child)
        return child

    def checkChildFile(self, childName, childSize):
        for child in self.children:
            if childName == child.name and child.type == 'FILE':
                child.setSize(childSize)
                return
        child = FileNode(name=childName, parent=self, size=childSize)
        self.addChild(child)

root = FileNode(name='root', dir=True)
current = root

def cd(val):
    global current
    if val == '/':
        current = root
        return
    if val == '..':
        current = current.getParent()
        return
    current = current.getChildDir(val)

def parseConsoleOutput(line):
    if line.startswith('dir'):
        current.getChildDir(line[4:])
        return
    size, name = line.split(' ')
    current.checkChildFile(name, int(size))

with open('input.txt') as f:
    data = f.read().splitlines()

for line in data:
    if line.startswith('$ cd'):
        cd(line[5:])
        continue
    if line.startswith('$ ls'):
        continue
    parseConsoleOutput(line)