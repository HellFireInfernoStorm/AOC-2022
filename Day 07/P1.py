from FileSys import *

total = 0

def getSize(node):
    global total
    size = 0
    for child in node.getChildren():
        if child.type == 'DIR':
            size += getSize(child)
        elif child.type == "FILE":
            size += child.size
    if size <= 100000:
        total += size
    return size

getSize(root)
print(total)