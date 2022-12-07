from FileSys import *

full_size = 70000000
min_size = 30000000

sizes = []

def getSize(node):
    size = 0
    for child in node.getChildren():
        if child.type == 'DIR':
            size += getSize(child)
        elif child.type == "FILE":
            size += child.size
    sizes.append(size)
    return size

used_size = getSize(root)
required_size = min_size - (full_size - used_size)

optimal = used_size

for size in sizes:
    if optimal > size >= required_size:
        optimal = size

print(optimal)